# BDC Client Request Template

Please provide a client evidence folder with the following minimum files:
- `README.md`
- primary packet JSON
- unified variant comparison CSV
- current runtime role mapping CSV
- current slice metrics CSV
- failure registry CSV or Markdown
- prompt/stage matrix CSV
- design priorities Markdown

Rules:
- mark every field as `measured`, `measured_from_historical_report`, `inferred`, or `missing`
- do not hide failed variants
- keep raw metric text when values are sparse or verdict-like
- keep current runtime truth separate from historical prior evidence
