from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)


def read_skill_name(skill_md: Path) -> str | None:
    text = skill_md.read_text(encoding="utf-8")
    match = NAME_PATTERN.search(text)
    if not match:
        return None
    return match.group(1).strip()


def validate() -> int:
    errors: list[str] = []

    if not SKILLS_DIR.exists():
        errors.append("Diretorio 'skills' nao encontrado.")
    else:
        for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
            if not skill_dir.name.startswith("kiss-"):
                errors.append(
                    f"{skill_dir.relative_to(ROOT)}: pasta deve usar prefixo 'kiss-'."
                )

            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                errors.append(f"{skill_dir.relative_to(ROOT)}: arquivo SKILL.md ausente.")
                continue

            skill_name = read_skill_name(skill_md)
            if not skill_name:
                errors.append(f"{skill_md.relative_to(ROOT)}: campo 'name' nao encontrado.")
                continue

            if skill_name != skill_dir.name:
                errors.append(
                    f"{skill_md.relative_to(ROOT)}: campo 'name' "
                    f"('{skill_name}') difere da pasta ('{skill_dir.name}')."
                )

            # Validar agentes
            agents_dir = skill_dir / "agents"
            if not agents_dir.exists():
                errors.append(f"{skill_dir.relative_to(ROOT)}: pasta 'agents' ausente.")
            else:
                for agent_file in ["openai.yaml", "gemini.yaml"]:
                    if not (agents_dir / agent_file).exists():
                        errors.append(
                            f"{skill_dir.relative_to(ROOT)}: arquivo "
                            f"agents/{agent_file} ausente."
                        )

    if errors:
        print("Validacao falhou:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validacao concluida com sucesso.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
