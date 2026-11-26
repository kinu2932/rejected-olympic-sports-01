# rejected-olympic-sports-01: one funny single-line sport the Olympics rejected.
# Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
# when run outside the grader's container). No network, no randomness:
# every run writes the same bytes. The line is 116 characters: three
# punchlines stacked on one pattern — the unsubscribe mechanism defeats
# itself (race to leave, first place wins MORE mail, the mail confirms it).
import os

JOKE = "Competitive unsubscribing: athletes race to leave a mailing list \u2014 first place wins three more emails confirming it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)

print(JOKE)
