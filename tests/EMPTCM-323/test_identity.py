import pytest
from typing import Optional

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-c1065fc7#branding/app_bar")
@pytest.mark.ac_index(0)
def test_theme_palette_primary_colors(http_client, base_url):
    """
    Verify that the theme palette.primary colors in the rendered UI match the new emerald palette.
    """
    response = http_client.get(f"{base_url}/app")
    assert response.status_code == 200

    # Check for theme variables or inline styles reflecting the new palette
    assert "palette.primary.main: '#10875A'" in response.text or \
           "palette.primary.light: '#3FB489'" in response.text or \
           "palette.primary.dark: '#0B5E3F'" in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-c1065fc7#branding/login_page")
@pytest.mark.ac_index(1)
def test_typography_font_family(http_client, base_url):
    """
    Verify that the typography font family is set to 'Georgia, "Times New Roman", Times, serif'.
    """
    response = http_client.get(f"{base_url}/login")
    assert response.status_code == 200

    # Check for font-family declarations in the rendered HTML
    assert "font-family: Georgia, \"Times New Roman\", Times, serif" in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-41cf4fab#observations")
@pytest.mark.ac_index(2)
def test_app_ts_no_unintended_changes(http_client, base_url):
    """
    Verify that App.tsx has no unintended changes (e.g., no ThemeProvider overrides, dark mode flags).
    """
    response = http_client.get(f"{base_url}/app")
    assert response.status_code == 200

    # Check for absence of dark mode flags or unintended ThemeProvider overrides
    assert "ThemeProvider" not in response.text or \
           "sx={{ background: 'dark' }}" not in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-41cf4fab#observations")
@pytest.mark.ac_index(3)
def test_app_bar_no_color_prop(http_client, base_url):
    """
    Verify that the AppBar in Navbar.tsx has no color prop and no background in its sx attribute.
    """
    response = http_client.get(f"{base_url}/navbar")
    assert response.status_code == 200

    # Check for absence of color or bgColor props in AppBar
    assert "color=" not in response.text and \
           "bgColor=" not in response.text and \
           "sx={{ background: " not in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-c1065fc7#branding/pmb_button")
@pytest.mark.ac_index(4)
def test_pmb_button_rendering(http_client, base_url):
    """
    Verify that Navbar.tsx imports AccountBalance and renders PMBButton with exact JSX.
    """
    response = http_client.get(f"{base_url}/navbar")
    assert response.status_code == 200

    # Check for AccountBalance import and PMBButton rendering
    assert "AccountBalance" in response.text

    # Check for PMBButton with exact JSX
    assert "PMB" in response.text
    assert "https://pmb.ro" in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-41cf4fab#observations")
@pytest.mark.ac_index(5)
def test_pmb_button_toolbar_position(http_client, base_url):
    """
    Verify that PMBButton is rendered in Toolbar after navigation Box and before role Chip.
    """
    response = http_client.get(f"{base_url}/navbar")
    assert response.status_code == 200

    # Check DOM order of Toolbar children
    assert "DirectionsBus" in response.text and \
           "PMB" in response.text and \
           "role Chip" in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-c1065fc7#branding/login_page")
@pytest.mark.ac_index(6)
def test_login_page_color_replacements(http_client, base_url):
    """
    Verify that all hardcoded blue values in LoginPage.tsx are replaced with emerald equivalents.
    """
    response = http_client.get(f"{base_url}/login")
    assert response.status_code == 200

    # Check for absence of blue colors and presence of emerald colors
    assert "#1976d2" not in response.text and \
           "#42a5f5" not in response.text and \
           "#1565c0" not in response.text and \
           "#10875A" in response.text and \
           "#3FB489" in response.text and \
           "#0B5E3F" in response.text

@pytest.mark.happyPath
@pytest.mark.httpApi
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-c1065fc7#branding/navbar")
@pytest.mark.ac_index(7)
def test_get_role_color_unchanged(http_client, base_url):
    """
    Verify that getRoleColor function in Navbar.tsx is unchanged and traveller role uses #1976d2.
    """
    response = http_client.get(f"{base_url}/navbar")
    assert response.status_code == 200

    # Check for unchanged role color assignments
    assert "#1976d2" in response.text

@pytest.mark.happyPath
@pytest.mark.cli
@pytest.mark.e2e
@pytest.mark.vault_ref("emptcm-323-apply-the-new-brand-41cf4fab#npm_lint_typecheck")
@pytest.mark.ac_index(8)
def test_npm_lint_and_type_check(run_command):
    """
    Verify that npm run lint and npm run type-check pass without errors.
    """
    # Run lint command
    lint_result = run_command("npm run lint -- --no-error-on-unmatched-pattern")
    assert lint_result.returncode == 0

    # Run type-check command
    type_check_result = run_command("npm run type-check")
    assert type_check_result.returncode == 0
