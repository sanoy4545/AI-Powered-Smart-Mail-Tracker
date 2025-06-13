# test_summarizer.py

from summarizer import summarize_and_categorize

# Sample email texts to test
sample_emails = [
    {
        "text": """
Dear Sanoy,

Congratulations! You’ve been selected for the AI Research Internship at KPMG. Your internship will start on July 1st, and we expect your onboarding documents to be completed by June 20th. Let us know if you have any questions.

Regards,  
HR Team
""",
        "description": "Test case: Internship offer (should be Very Important)"
    },
    {
        "text": """
Hello,

Your LinkedIn job alert: 5 new Python Developer jobs near Kochi.  
Apply today to get matched with top roles!

Cheers,  
LinkedIn
""",
        "description": "Test case: Job alert (likely Low priority)"
    },
    {
        "text": """
Hi Team,

Reminder: Our weekly sprint review is scheduled for Thursday at 4 PM. Please ensure all Jira tasks are updated.

Thanks,  
Ananya
""",
        "description": "Test case: Project reminder (should be High priority)"
    },
    {
        "text": "",  # Edge case
        "description": "Test case: Empty body"
    }
]

# Run test cases
for idx, sample in enumerate(sample_emails):
    print(f"\n🧪 {sample['description']}")
    result = summarize_and_categorize(sample["text"])  
    print(f"Summary: {result.get('summary')}")
    print(f"Priority: {result.get('priority')}")
    if result.get("error"):
        print(f"Error: {result.get('error')}")
