"""Pydantic model representing Hyprland workspaces.

This module provides a way to query Hyprland workspaces. The workspace objects are
constructed by parsing the output from the `hyprctl` command-line utility.

Classes:
    Workspace: Represents a workspace, and contains all available information about the workspace.
"""

from pydantic import BaseModel, Field

from pyprland.validators.common import HexString


class Workspace(BaseModel):
    """Represents a workspace in the Hyprland wayland compositor.

    The class allows reading of workspace attributes.

    Attributes:
        id (int): Numeric ID of the workspace.
        name (str): Name assigned to the workspace.
        monitor_name (str): Name of the monitor which this workspace is on.
        last_window_address (str): Address string of the most recently active window on the workspace.
        last_window_title (str): Title of the most recently active window on the workspace.
        window_count (int): Number of windows placed in the workspace.
        has_fullscreen (bool): True if at least one window in the workspace is in fullscreen mode.
    """
    id: int
    name: str
    monitor_name: str = Field(..., alias="monitor")
    last_window_address: HexString = Field(..., alias="lastwindow")
    last_window_title: str = Field(..., alias="lastwindowtitle")
    window_count: int = Field(..., alias="windows")
    has_fullscreen: bool = Field(..., alias="hasfullscreen")


    @property
    def last_window_address_as_int(self) -> int:
        """Returns the integer representation of the window's `last_window_address` property."""

        return int(self.last_window_address, 16)


    def __repr__(self):
        return f"<Workspace(id={self.id}, name={self.name!r})>"