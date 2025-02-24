import pandas as pd

# Load financial data (Ensure 'financials.csv' is in the working directory)
df = pd.read_excel("Financials.xlsx")

# Function to get total revenue
def get_total_revenue():
    total_revenue = df["revenue (billion $)"].sum()
    return f"The total revenue is {total_revenue:.2f} billion $."

# Function to get net income change (assuming we have a 'previous year net income' column)
def get_net_income_change():
    if "previous year net income (billion $)" in df.columns:
        net_income_change = df["net income (billion $)"] - df["previous year net income (billion $)"]
        total_change = net_income_change.sum()
        direction = "increased" if total_change > 0 else "decreased"
        return f"The net income has {direction} by {abs(total_change):.2f} billion $ over the last year."
    else:
        return "Sorry, I don't have the previous year's net income data to compare."

# Simple chatbot function
def simple_chatbot(user_query):
    user_query = user_query.lower().strip()
    if user_query == "what is the total revenue?":
        return get_total_revenue()
    elif user_query == "how has net income changed over the last year?":
        return get_net_income_change()
    elif user_query == "what is the highest operating income?":
        highest_income = df["operating income (billion $)"].max()
        return f"The highest operating income is {highest_income:.2f} billion $."
    elif user_query == "which company spends the most on r&d?":
        top_rd_company = df.loc[df["r&d spending (billion $)"].idxmax(), "company"]
        return f"The company that spends the most on R&D is {top_rd_company}."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Run chatbot in CLI
if __name__ == "__main__":
    print("Welcome to the financial chatbot! Type 'exit' to end.")
    while True:
        query = input("Ask a financial question: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        response = simple_chatbot(query)
        print(response)
