def format_llm_job_summary(response):
    summary_dict = response.model_dump()

    formatted = "\n".join([
    f"Company name: {summary_dict.get('company')}",
    f"\nSalary:\n{summary_dict.get('salary')}",
    f"\nResponsibilities:\n{', '.join(summary_dict.get('responsibilities'))}",
    f"\nBenefits:\n{', '.join(summary_dict.get('benefits'))}",
    f"\nRequired skills:\n{', '.join(summary_dict.get('required_skills'))}",
    f"\nDesirable skills:\n{', '.join(summary_dict.get('desirable_skills'))}",
    f"\nExperience needed:\n{summary_dict.get('experience_needed')}"
])
    return formatted