-- Use only when setting up the project's DB.

INSERT INTO auth_group (name)
VALUES
    ('ADMINISTRATEUR'),
    ('REFERENTE_ADMINISTRATIVE'),
    ('FORMATEUR'),
    ('ELEVE')
ON CONFLICT (name) DO NOTHING;