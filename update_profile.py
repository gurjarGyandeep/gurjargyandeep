from github import Github
import os

# Get GitHub token from environment variables
token = os.getenv('GITHUB_TOKEN')
g = Github(token)

# Get the user
user = g.get_user()

# Generate the new README content
readme_content = f"# {user.name}'s GitHub Profile\n\n"
readme_content += "👋 Hello, I'm Gyandeep!\n\n"
readme_content += "🔍 **About Me**\nI'm a passionate data enthusiast with experience in SQL, Python, Tableau, Snowflake, and Power BI.\n\n"
readme_content += "💼 **Professional Background**\n\n"
readme_content += "- **SQL**: Proficient in writing complex queries, optimizing database performance, and managing relational databases.\n"
readme_content += "- **Python**: Skilled in data analysis, scripting, and building data-driven applications using libraries like pandas, numpy, and matplotlib.\n"
readme_content += "- **Tableau**: Experienced in creating interactive and insightful dashboards for data visualization and business intelligence.\n"
readme_content += "- **Snowflake**: Knowledgeable in using Snowflake for data warehousing, including data loading, transformation, and querying.\n"
readme_content += "- **Power BI**: Proficient in DAX queries, using Power BI Query Editor, and creating automated dashboards to monitor product health.\n\n"
readme_content += "📊 **Projects**\n\n"

for repo in user.get_repos():
    if not repo.fork:  # Avoid including forked repositories
        readme_content += f"- **[{repo.name}]({repo.html_url})**: {repo.description or 'No description provided.'}\n"

readme_content += "\n🌱 **Currently Learning**\nI'm currently diving deeper into machine learning and big data technologies to enhance my data science toolkit.\n\n"
readme_content += "📫 **Get in Touch**\nEmail: [mail2gyandeep96@gmail.com]\n\n"

# Update the README file in the repository
repo = g.get_repo(f"{user.login}/{user.login}")
contents = repo.get_contents("README.md")
repo.update_file(contents.path, "Update README.md", readme_content, contents.sha)
