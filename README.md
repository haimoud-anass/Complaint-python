# Système de Gestion des Réclamations

Un système de gestion des réclamations basé sur Python qui permet aux utilisateurs de soumettre, suivre et gérer les réclamations avec des interfaces utilisateur et administrateur.

## Fonctionnalités

### Fonctionnalités Utilisateur
- Système d'inscription et de connexion utilisateur
- Soumettre de nouvelles réclamations avec descriptions
- Voir le statut et la résolution des réclamations
- Mettre à jour les réclamations existantes
- Suivre le temps d'exécution des réclamations

### Fonctionnalités Administrateur
- Tableau de bord administrateur avec gestion complète des réclamations
- Voir toutes les réclamations dans un tableau détaillé
- Ajouter, mettre à jour et supprimer des réclamations
- Gérer le statut et la résolution des réclamations
- Suivre les mises à jour et les temps d'exécution des réclamations

## Détails Techniques

### Configuration Système Requise
- Python 3.x
- SQLite3
- Tkinter (inclus dans la bibliothèque standard Python)

### Structure de la Base de Données
Le système utilise une base de données SQLite (`Complaints.db`) avec le schéma suivant :
- ID (Auto-incrément)
- Nom d'utilisateur
- Mot de passe
- Description
- Statut
- Résolution
- Temps d'exécution
- Statut de mise à jour

### Structure du Projet
```
Complaint-python/
├── README.md
├── Complaints.db
└── Le Code Du Programme/
    ├── main.py              # Point d'entrée principal de l'application
    ├── Admin_Zone.py        # Implémentation de l'interface administrateur
    ├── II.HTML             # Interface web
    ├── js.js               # Fonctionnalités JavaScript
    └── image1.ico          # Icône de l'application
```

## Installation

1. Clonez le dépôt :
```bash
git clone [url-du-dépôt]
```

2. Accédez au répertoire du projet :
```bash
cd Complaint-python
```

3. Exécutez l'application :
```bash
python "Le Code Du Programme/main.py"
```

## Utilisation

### Accès Utilisateur
1. Lancez l'application
2. Inscrivez-vous avec un nouveau compte ou connectez-vous avec des identifiants existants
3. Soumettez de nouvelles réclamations ou consultez les réclamations existantes
4. Mettez à jour les détails des réclamations selon vos besoins

### Accès Administrateur
1. Lancez l'application
2. Connectez-vous avec les identifiants administrateur (nom d'utilisateur : "admin", mot de passe : "admin")
3. Accédez au tableau de bord administrateur
4. Gérez toutes les réclamations via l'interface

## Fonctionnalités de Sécurité
- Protection par mot de passe des comptes utilisateurs
- Accès réservé aux administrateurs pour les fonctionnalités de gestion
- Stockage sécurisé dans la base de données
- Validation des entrées pour tous les formulaires

## Contribution
N'hésitez pas à soumettre des problèmes et des demandes d'amélioration !

## Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
