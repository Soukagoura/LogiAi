# ADR 003 : sécurité de l'API LogiAI

## Décision 1 : où transmettre la clé (en-tête, URL ou corps) ?
- Choix : l'en-tête X-API-Key.
- Ce que l'autre option ferait perdre : une URL est enregistrée partout (journaux du serveur, historique du navigateur) ; le corps ne convient pas aux requêtes GET comme /v1/model-info.

## Décision 2 : quelles origines autoriser (CORS) ?
- Choix : une liste précise (config.ALLOWED_ORIGINS).
- Ce que l'autre option ferait perdre : « * » autoriserait n'importe quel site à appeler l'API depuis le navigateur d'un utilisateur ; on perd tout contrôle sur qui peut l'utiliser.
