# TextAI_Auto V2.3 BDC Evaluation Checklist

## Intake Gate
- [ ] Folder root exists
- [ ] All required files are present
- [ ] README names the exact experiment id and arms
- [ ] Deploy/runtime truth note exists
- [ ] No unresolved file naming ambiguity

## Evidence Integrity
- [ ] Evidence labels are explicit
- [ ] Failed variants are included
- [ ] Current runtime truth is separated from historical prior
- [ ] Commit/deploy truth is reconciled or explicitly marked unresolved

## Architecture Gate
- [ ] 4-role framework preserved
- [ ] No harmonizer added
- [ ] No extra role expansion introduced
- [ ] Guardian remains post-edit unless separately justified

## Product Outcome Gate
- [ ] Compare Arm A vs Arm B vs Arm C in one table
- [ ] Check `forensic_high_ai_5` accepted rewrite rate
- [ ] Check `mid_ai_4` useful output rate
- [ ] Check RU accepted-output safety
- [ ] Check EN accepted-output retention

## Safety Gate
- [ ] Zero accepted harmful outputs
- [ ] Zero severe RU lexical fusion in accepted outputs
- [ ] Zero severe connector corruption in accepted outputs
- [ ] No material semantic safety regression

## Planner / Editor / Guardian Observability Gate
- [ ] Planner decisions visible per case
- [ ] Editor prompt family visible per case
- [ ] Guardian accept/revert/retry reason visible per case
- [ ] Route/intensity/skip signals captured

## BDC Decision Gate
- [ ] Does Arm B beat Arm A?
- [ ] Does Arm C recover useful mid-AI activity?
- [ ] If not, is failure editor-driven rather than architecture-driven?
- [ ] Is any guardian threshold review actually supported by evidence?

## Output Gate
- [ ] `client-bundle` run succeeds
- [ ] Recommendation generated
- [ ] Redesign guidance generated
- [ ] Measurement gaps updated
- [ ] Client-ready memo generated

## Final Verdict Categories
Use one only:
- `SUCCESS`
- `PARTIAL`
- `FAILURE`

### SUCCESS
- rewrite lift exists
- safety preserved
- no role expansion required

### PARTIAL
- some editor improvement or slice recovery exists
- but lift is incomplete or below threshold

### FAILURE
- no rewrite lift over control
- or harmful accepted outputs appear
- or packet truth is not reliable enough for architectural judgment
