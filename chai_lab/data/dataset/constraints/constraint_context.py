from dataclasses import asdict, dataclass
from typing import Any

from chai_lab.data.features.generators.docking import (
    ConstraintGroup as DockingConstraint,
)
from chai_lab.data.features.generators.token_dist_restraint import (
    ConstraintGroup as ContactConstraint,
)
from chai_lab.data.features.generators.token_pair_pocket_restraint import (
    ConstraintGroup as PocketConstraint,
)
from chai_lab.utils.typing import typecheck


@typecheck
@dataclass
class ConstraintContext:
    docking_constraints: list[DockingConstraint] | None
    contact_constraints: list[ContactConstraint] | None
    pocket_constraints: list[PocketConstraint] | None

    def to_dict(self) -> dict[str, Any]:
        return dict(
            docking_constraints=[asdict(c) for c in self.docking_constraints]
            if self.docking_constraints is not None
            else [None],
            contact_constraints=[asdict(c) for c in self.contact_constraints]
            if self.contact_constraints is not None
            else [None],
            pocket_constraints=[asdict(c) for c in self.pocket_constraints]
            if self.pocket_constraints is not None
            else [None],
        )

    @classmethod
    def empty(cls) -> "ConstraintContext":
        return cls(
            docking_constraints=None,
            contact_constraints=None,
            pocket_constraints=None,
        )
