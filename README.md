# Members:
  1. Jeremy Barcos
  2. Raj Flores
  3. James Gica
  4. Raphael Magaso

## MILESTONE I
### Context: 
Managing daily expenses is something a lot of students struggle with. Most of us try to budget 
using notebooks or phone memos, but it’s easy to lose track of where the money actually goes. 
Having a simple system that records income and expenses in one place would make personal 
budgeting more organized and manageable. 

### Problems/Needs Analysis: 
Right now, students don’t have a convenient tool for tracking their spending. Writing everything 
down manually is inconsistent, and spreadsheet tracking takes extra effort. Without an easy way 
to log transactions, it’s hard to see spending patterns or calculate balances. The need is for a 
straightforward database-backed system that can save, retrieve, and summarize financial data. 

### Solution:
We propose building the Expense Tracker API, a RESTful web service that lets users manage 
their income and expenses. It will include endpoints to add transactions, view spending history, 
generate summaries, and delete entries. Each record will include details like description, 
amount, category, type (income or expense), and date. The API can also compute total income, 
total expenses, and remaining balance. Later, it can be connected to a simple dashboard that 
shows charts or summaries to help users understand their financial habits better.
