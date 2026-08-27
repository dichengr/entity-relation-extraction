# Third-party components

`rel_pipe.py` and `rel_model.py` are vendored unmodified from Explosion's
`rel_component` tutorial:
https://github.com/explosion/projects/tree/v3/tutorials/rel_component

They register the `relation_extractor` factory and the `rel_model.v1` /
`rel_instance_tensor.v1` / `rel_classification_layer.v1` architectures that
`configs/rel_tok2vec.cfg` refers to. spaCy cannot load the relation config without them.

`custom_functions.py` registers the `Gold_ents_Corpus.v1` reader the config uses.

Licensed MIT by Explosion AI. The tutorial's `parse_data.py` targets a biomedical
label set and is not vendored.

## Local modifications

Two, both compatibility fixes rather than behaviour changes:

1. `custom_functions.py` - imports changed from `scripts.rel_pipe` / `scripts.rel_model`
   to `rel_pipe` / `rel_model`, since these files live flat in `src/` rather than in a
   `scripts` package.
2. `rel_model.py` - `create_classification_layer` was annotated `nO: int = None,
   nI: int = None`. Newer spaCy validates architecture configs with pydantic, which
   rejects `null` for an `int` field, so `spacy train` failed with
   "None is not <class 'int'>". Widened to `Optional[int]`; thinc still infers both
   dimensions during `initialize`.
