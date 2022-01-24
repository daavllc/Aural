from manager.command import Command

import objects.Route as rt

class CreateRoute(Command):
    def __init__(self, parent, index):
        self.parent = parent
        self.index = index
        self.route = rt.Route()

    def Details(self) -> str:
        return f"created route [{str(self.route.GetUUID())}]"

    def Execute(self) -> None:
        self.parent.Routes.append(self.route)

    def Undo(self) -> None:
        self.parent.Routes.remove(self.route)
        if self.parent.Selected == self.Selected == self.index:
            self.parent.Deselect()

    def Redo(self) -> None:
        self.parent.Routes.append(self.Route)

class SelectRoute(Command):
    def __init__(self, parent, prevRoute, prevIndex, currRoute, currIndex):
        self.parent = parent
        self.prevRoute = prevRoute
        self.prevIndex = prevIndex
        self.currRoute = currRoute
        self.currIndex = currIndex

    def Details(self) -> str:
        if self.prevRoute is None and self.currRoute is None:
            return f"changed selection from [None] to [None]"
        elif self.currRoute is None:
            return f"changed selection from [{self.prevRoute.GetUUID()}] to [None]"
        elif self.prevRoute is None:
            return f"changed selection from [None] to [{self.currRoute.GetUUID()}]"
        else:
            return f"changed selection from [{self.prevRoute.GetUUID()}] to [{self.currRoute.GetUUID()}]"

    def Execute(self) -> None:
        self.parent._Select(self.currIndex)

    def Undo(self) -> None:
        self.parent._Select(self.prevIndex)

    def Redo(self) -> None:
        self.parent._Select(self.currIndex)