"""EMPTCM-323: the brand identity lives in one place, App.tsx's createTheme call.
These tests read the web app's source files and hold before and after the
ticket is implemented."""

import re
from pathlib import Path

import pytest


def _repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "RouteOptimizer.Web").is_dir():
            return parent
    raise RuntimeError("RouteOptimizer.Web not found above this test file")


SRC = _repo_root() / "RouteOptimizer.Web" / "src"
APP = (SRC / "App.tsx").read_text(encoding="utf-8")
NAVBAR = (SRC / "components" / "common" / "Navbar.tsx").read_text(encoding="utf-8")
LOGIN = (SRC / "pages" / "LoginPage.tsx").read_text(encoding="utf-8")


@pytest.mark.happyPath
@pytest.mark.unitTest
@pytest.mark.inProcess
def test_theme_is_declared_once_in_app():
    """AC3: App.tsx holds exactly one createTheme call."""
    # ac_index: 1
    # vault_ref: none
    assert APP.count("createTheme(") == 1


@pytest.mark.happyPath
@pytest.mark.unitTest
@pytest.mark.inProcess
def test_primary_palette_has_main_light_and_dark():
    """AC1: palette.primary declares main, light and dark as hex colours."""
    # ac_index: 1
    # vault_ref: none
    for key in ("main", "light", "dark"):
        assert re.search(rf"\b{key}\s*:\s*['\"]#[0-9a-fA-F]{{6}}['\"]", APP), f"primary.{key} missing"


@pytest.mark.regression
@pytest.mark.unitTest
@pytest.mark.inProcess
def test_secondary_and_background_are_untouched():
    """AC1: palette.secondary stays '#dc004e' and background.default stays '#f5f5f5'."""
    # ac_index: 1
    # vault_ref: none
    assert "'#dc004e'" in APP
    assert "default: '#f5f5f5'" in APP


@pytest.mark.regression
@pytest.mark.unitTest
@pytest.mark.inProcess
def test_appbar_takes_its_colour_from_the_theme():
    """AC4: the AppBar has no colour prop, so it follows palette.primary."""
    # ac_index: 4
    # vault_ref: none
    appbar = re.search(r"<AppBar\b([^>]*)>", NAVBAR).group(1)
    assert "color=" not in appbar


@pytest.mark.errorPath
@pytest.mark.unitTest
@pytest.mark.inProcess
def test_login_page_does_not_mix_old_and_new_primary_colours():
    """AC7: LoginPage.tsx uses either the old MUI blues or the new burgundy set, never both."""
    # ac_index: 3
    # vault_ref: none
    old = any(c in LOGIN.lower() for c in ("#1976d2", "#42a5f5", "#1565c0"))
    new = any(c in LOGIN.lower() for c in ("#800020", "#a3324a", "#5c0017"))
    assert old != new
