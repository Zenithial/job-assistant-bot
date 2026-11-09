def format_llm_response(response):
    summary_dict = response.model_dump()
    
    education = ""
    all_education = summary_dict.get('education') or []
    for i in range(len(all_education)):
        education += "\n".join(
        f"  {key}: {value}"
        for key, value in all_education[i].items()
    )
        education += "\n\n"

    experience = ""
    prev_jobs = summary_dict.get('work_experience') or []
    for i in range(len(prev_jobs)):
        experience += "\n".join(
        f"  {key}: {value}"
        for key, value in prev_jobs[i].items()
        )
        experience += "\n\n"

    formatted = "\n".join([
    f"👤 Name: {summary_dict.get('name')}",
    f"\n📌 Background info:\n{summary_dict.get('background_info')}",
    f"\n🛠 Key strengths and skills:\n{summary_dict.get('key_strengths_and_skills')}",
    f"\n🎓 Education:\n{education}",
    f"\n💼 Work experience:\n{experience}",
    f"\n🌟 Personal interests and hobbies:\n{', '.join(summary_dict.get('personal_hobbies_and_interests', []))}"
])
    return formatted