from rich.cells import split_text
from hypothesis import given, settings
import hypothesis.strategies as st

@settings(max_examples=300, deadline=None)
@given(s=st.text(), pos=st.integers(min_value=1, max_value=10000))
def test_split_text_never_crashes(s, pos):
    split_text(s, pos)
