# System Design

## Objectiu del projecte
Hugo site amb control d'estat (open / closed / menu) basat en dades.

## Regles d'arquitectura
- Els partials han de retornar dades o render, mai ambdós.
- Qualsevol estat ha de ser un contracte explícit (dict o string, no HTML mixt).
- Evitar encadenament de partials sense control de tipus.

## Flux actual
data → partials → render index
