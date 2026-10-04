# Recorded single-scene workflow

Use this mode for a recorded Graph Engineering run. Existing specialist craft
instructions still apply. Resolve this skill directory through any symlink;
the repository root is two parents above the resolved skill directory. Load
`workflows/single-scene.v1.json` and the schemas in `schemas/` from that root.
Do not resolve those resources relative to the user's film project or copy the
skill alone: this workflow requires the complete installed repository.

Run `python scripts/validate_graph.py --help` from the repository root after
installing `requirements-graph.txt` in a virtual environment (Python 3.10+).
The validator is read-only. It neither starts agents nor sandboxes their writes.

## Contract

The workflow records node IDs, mandatory dependencies, exact output paths and
owners. Ownership uses the longest matching directory prefix: cinematography
is excluded from production-design ownership; qc/reviews is excluded from
supervisor ownership. `qc/reviews/` is reserved but unused in this profile;
review evidence lives beside the manifest, outside project/. Markdown contains creative work; JSON sidecars record
artifact versions, consumed hashes, runs and approvals. A pilot snapshot has
`manifest.json` beside its `project/` directory. Every project file must be
registered, except regular Finder `.DS_Store` metadata files; administrative logs belong beside the manifest, not in project/.

The first version is a one-scene preproduction profile. Final editing and media
production remain available as existing skills but are outside this profile.
The exact paths are for scene-01; create a new versioned workflow for other
scopes rather than silently changing a running contract.

## Scheduling and gates

1. Produce brief, script and direction. Record direction approval against its
   output and input hashes before starting design drafts.
2. Character, production and camera drafts consume the same approved script
   and direction snapshot. They may run in parallel, but must not consume one
   another's unfinished outputs. Serial execution is also valid; record actual
   actors and times rather than claiming parallel execution.
3. The supervisor records a joint design decision after all three drafts.
   Quote conflicts; the director/user resolves them. Each specialist changes
   only its own output. A passing design review must declare `approver_role`
   as `director` or `user`; `coordinator` cannot approve it. This role is an
   operator declaration, not authenticated identity or independent review.
   Failed approval blocks canon publication. Corrections
   create a new snapshot; keep the rejected checkpoint for evidence.
4. Publish locked canon only after design approval. Storyboard consumes canon;
   shots consume storyboard; final image/video prompts consume shots and canon.
   Sound consumes shots. These deliberately coarse file dependencies are
   conservative: a visual change can invalidate sound through the shot list.
5. An independent reviewer checks the complete package and exact hashes in a
   `gate: package` review. A different role name in the same author session is
   not independent. Gate coordinator checks are not independent final review.
   Store reviewer evidence outside project/, then import the exact review into
   the manifest without inventing a passing verdict.

## Validation and revision

- `validate --manifest PATH --partial`: a checkpoint with no dependent run past
  a failed/missing gate; not a production approval.
- `validate --manifest PATH --pre-review`: full structural validation before
  independent review; not a production approval.
- `validate --manifest PATH`: full validation including independent review.
- `validate --manifest PATH --legacy-approvals`: historical compatibility audit
  for old records missing a design approver role. The result explicitly says
  it is not production approval. Never fabricate a role on an old review.
- `impact --manifest PATH --changed production`: list the changed artifact and
  every transitive consumer; approval of old hashes never approves new content.
- `revision --previous OLD --manifest NEW --record CHANGE`: verify previous
  manifest hash, impact closure, incremented revisions and unchanged reuse.
  Validate both packages separately as well; this command checks lineage only.
  `--allow-growth` permits a partial checkpoint to add first-run artifacts
  (revision 1) but never remove old ones. `affected` and `rerun_nodes` then
  include those new artifacts/nodes as well as the revised existing nodes.
  The Python API takes the previous manifest path and verifies its raw bytes
  against the recorded hash itself.

Run validation before crossing a gate and before handoff. Failed or interrupted
attempts are evidence beside the manifest; never register their partial outputs
as successful artifacts. Resume from a new successful attempt; keep unaffected
artifacts and run records unchanged. Do not overwrite previous snapshots.
The operator compares before/after filesystem differences to catch writes
outside the registered project tree; ownership declarations are not access control.

JSON identity and timestamp fields are audit records supplied by operators,
not authenticated signatures. The validator cannot prove creative quality,
truthful actor identity, real chronology or external approvals. Final review
must inspect the work and its actual execution evidence.

## Deliberate v1 scope reductions

Artifacts do not store a mutable status field: availability, staleness and
approval are derived from files, hashes, inputs and reviews. Run status records
only succeeded/failed; pending/running scheduling is not implemented. A run's
skill is obtained through node_id → workflow owner rather than duplicated.
There is no shot_id field because this profile registers scene-level documents
containing all three shots. Per-shot scheduling requires a new profile.
Timestamps must contain a timezone and use RFC3339 syntax; enforcement does not
depend on optional jsonschema format packages. They still prove only declared
chronology, not actual production duration or a real human approval pause.
