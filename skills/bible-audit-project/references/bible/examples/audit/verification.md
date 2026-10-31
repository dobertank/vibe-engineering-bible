# Reproduce the evidence

Use a local checkout, a POSIX shell and standard `find`, `nl`, `cat`, `grep`, `sed`, `cp`, and `mktemp`. From the Bible root:

```sh
bible_root="$PWD"
fixture="$bible_root/examples/audit/fixture"
find "$fixture" -type f -print
nl -ba "$fixture/README.md"
cat "$fixture/glossary.md"
for name in AGENTS.md CLAUDE.md; do
  if test -f "$fixture/$name"; then
    printf 'present: %s\n' "$name"
  else
    printf 'absent: %s\n' "$name"
  fi
done
```

Expect only `README.md` and `glossary.md`. README lines 5 and 7 confirm A-001. Both presence checks print `absent`, confirming A-002 within the fixture root. `cat` prints the two fictional terms, verifying the README's run command. The order from `find` does not matter.

## Fix one finding and recheck its boundary

Use a temporary copy so the original evidence remains reproducible. These commands write only into a new temporary directory:

```sh
audit_scratch=$(mktemp -d)
cp -R "$fixture" "$audit_scratch/project"
sed 's/Level: Prototype\. Customers: no\. Lifecycle: prototype\./Level: Production. Customers: no. Lifecycle: production./' \
  "$audit_scratch/project/README.md" > "$audit_scratch/README.fixed.md"
cp "$audit_scratch/README.fixed.md" "$audit_scratch/project/README.md"
grep -n '^Level: Production\.' "$audit_scratch/project/README.md"
if test ! -f "$audit_scratch/project/AGENTS.md" && test ! -f "$audit_scratch/project/CLAUDE.md"; then
  printf 'A-002 remains: baseline absent\n'
fi
printf 'Temporary copy: %s\n' "$audit_scratch"
```

Expect `5:Level: Production. Customers: no. Lifecycle: production.` and `A-002 remains: baseline absent`. A-001 is fixed; the project still does not meet DoD.

Negative control: create an empty file **only in the temporary copy**:

```sh
: > "$audit_scratch/project/AGENTS.md"
if test -f "$audit_scratch/project/AGENTS.md"; then
  printf 'Presence check passes; baseline content is NOT validated\n'
fi
```

Expect the stated line. An empty file passes a presence check but is not a completed baseline: this demonstrates the evidence boundary, not a fix for A-002. Remove the printed temporary directory after inspecting it.
