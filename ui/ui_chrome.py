"""App-specific CSS shared by both PennyCore Streamlit surfaces.

`ui_theme` carries the design system itself (paper ground, Fraunces / Inter /
JetBrains Mono, the teal accent, and every native Streamlit widget). It is a
verbatim copy of the portfolio-wide theme file, so anything that is true of
*these two apps only* — the bordered queue rows, the N-of-M quorum bar, the
JSON state panels of the demo timeline — lives here instead, and both apps get
one identical look from one file.

Usage, immediately after ``st.set_page_config(...)``::

    ui_theme.apply_theme()
    ui_chrome.apply_app_css()

Presentation only: every rule below is colour, radius, spacing or type, and
every value comes from the ``:root`` tokens ``ui_theme`` declares. Selectors
hang off Streamlit's stable ``data-testid`` / ``data-baseweb`` hooks, never the
generated emotion class names, and font-family is never set on ``span`` or
``*`` — that breaks the Material icon ligatures.
"""

from __future__ import annotations

import streamlit as st

APP_CSS = """
<style>
/* the sidebar title reads as a panel label, not a second page title */
[data-testid="stSidebar"] h1 { font-size: 1.25rem; }

/* queue rows and the active timeline step: st.container(border=True). The
   frame comes from a generated class and every vertical block shares this
   wrapper, so nothing marks the bordered ones; only properties that stay
   invisible on a borderless wrapper are set — the paper line and card radius. */
[data-testid="stVerticalBlockBorderWrapper"] {
  border-color: var(--line); border-radius: 16px; }

/* the N-of-M quorum bar is the number these screens exist to show. Target the
   bar itself: stProgress also holds the text label as a sibling div, so a bare
   `> div > div` chain would squash that label to the bar's height. */
[data-testid="stProgress"] [data-baseweb="progress-bar"] > div > div {
  background: var(--paper-alt) !important; border-radius: 999px; height: 9px; }
[data-testid="stProgress"] [data-baseweb="progress-bar"] > div > div > div {
  background: var(--accent) !important; border-radius: 999px; }
[data-testid="stProgress"] p {
  font-family: 'JetBrains Mono', ui-monospace, Consolas, monospace;
  font-size: .68rem; font-weight: 600; letter-spacing: .1em;
  text-transform: uppercase; color: var(--ink-3); }

/* status alerts: the portfolio's ok / warn / bad / info, always on their tint.
   Streamlit paints the tint on the outer container; the kind is only named on
   an inner child, hence :has(). */
[data-testid="stAlertContainer"] { border: 1px solid transparent; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentInfo"]) {
  background-color: rgba(47, 95, 138, .09); border-color: rgba(47, 95, 138, .22); color: #2f5f8a; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentSuccess"]) {
  background-color: rgba(63, 122, 58, .10); border-color: rgba(63, 122, 58, .25); color: #3f7a3a; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentWarning"]) {
  background-color: rgba(168, 106, 18, .10); border-color: rgba(168, 106, 18, .25); color: #a86a12; }
[data-testid="stAlertContainer"]:has([data-testid="stAlertContentError"]) {
  background-color: rgba(179, 38, 30, .08); border-color: rgba(179, 38, 30, .22); color: #b3261e; }
[data-testid="stAlertContainer"] p, [data-testid="stAlertContainer"] li { color: inherit; }

/* blockquote — the planner's reasoning, on both screens */
[data-testid="stMarkdownContainer"] blockquote {
  border-left: 2.5px solid var(--accent); background: var(--accent-tint);
  border-radius: 0 10px 10px 0; padding: .55rem .9rem; margin: .5rem 0;
  color: var(--ink-2); font-style: normal; }

/* the audit trail reads as a list of timestamps — mono, muted, tight */
[data-testid="stMarkdownContainer"] li code,
[data-testid="stCaptionContainer"] code {
  color: var(--ink-3); background: var(--paper-alt);
  border: 1px solid var(--line); }

/* JSON state panels on the demo timeline */
[data-testid="stJson"] { background: var(--card); border: 1px solid var(--line);
  border-radius: 12px; padding: .5rem .75rem; box-shadow: var(--shadow-sm); }
[data-testid="stDataFrame"] { box-shadow: var(--shadow-sm); }

/* dropdown menus */
ul[role="listbox"] { border-radius: 12px !important;
  border: 1px solid var(--line) !important; background: var(--card) !important;
  box-shadow: var(--shadow-md) !important; padding: 5px !important; }
li[role="option"] { border-radius: 999px !important; font-size: .9rem !important; }
li[role="option"]:hover, li[role="option"][aria-selected="true"] {
  background: var(--accent-tint) !important; color: var(--accent) !important; }
</style>
"""


def apply_app_css() -> None:
    """Inject the two apps' shared, app-specific rules on top of ui_theme."""
    st.markdown(APP_CSS, unsafe_allow_html=True)
