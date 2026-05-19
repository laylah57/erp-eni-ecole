-- Use only when setting up the project's DB, after running Django's migrations to make sure the tables are created.

INSERT INTO auth_group (name)
VALUES
    ('ADMINISTRATEUR'),
    ('REFERENTE_ADMINISTRATIVE'),
    ('FORMATEUR'),
    ('ELEVE')
ON CONFLICT (name) DO NOTHING;