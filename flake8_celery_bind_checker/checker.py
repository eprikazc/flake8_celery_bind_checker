import ast
from flake8_plugin_utils import Error, Plugin, Visitor


class UnBoundTaskWithSelf(Error):
    code = "CBL001"
    message = "Celery task without 'bind=True' still declares 'self' as its first argument."


class BoundTaskWithoutSelf(Error):
    code = "CBL002"
    message = "Celery task with 'bind=True' must have 'self' as its first argument."


class CeleryBindVisitor(Visitor):
    def visit_FunctionDef(self, node):
        # This method inspects function definitions

        for decorator in node.decorator_list:
            try:
                is_celery_task = (
                    hasattr(decorator, "id") and decorator.id == "shared_task"
                    or decorator.func.id == "shared_task"
                )
            except AttributeError:
                is_celery_task = False
            if not is_celery_task:
                continue
            is_bound = False
            if hasattr(decorator, "func"):
                for kw in decorator.keywords:
                    if kw.arg == "bind":
                        bind_value = isinstance(kw.value, ast.NameConstant) and kw.value.value
                        is_bound = bind_value
                        break

            if is_bound:
                if not node.args.args or node.args.args[0].arg != "self":
                    self.error_from_node(
                        BoundTaskWithoutSelf,
                        node,
                    )
            else:
                if node.args.args and node.args.args[0].arg == "self":
                    self.error_from_node(
                        UnBoundTaskWithSelf,
                        node=node,
                    )
        self.generic_visit(node)


class CeleryBindPlugin(Plugin):
    name = "flake8_celery_bind_checker"
    version = "0.1.0"
    visitors = [CeleryBindVisitor]
