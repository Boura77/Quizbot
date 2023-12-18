# Quizbot
This quizbot will ask 10 mcq questions based on the users choice of topic
AGI Quiz Application
This Streamlit web application serves as an Artificial General Intelligence (AGI) Quiz Application, leveraging the OpenAI GPT-3.5 Turbo model to conduct a quiz. The application is designed to generate Single Correct Multiple Choice Questions (MCQs) on a user-specified topic.

Features
Expert Assistant: The application assumes the role of an expert in creating and conducting Single Correct MCQs. The assistant provides guidance on the quiz format and rules.

Interactive Quiz: Users can engage in an interactive quiz by responding to each question presented by the assistant. The correct answers are not revealed immediately to maintain the quiz experience.

Progressively Difficult Questions: The quiz is designed to escalate in difficulty progressively, ensuring an engaging and challenging experience for the user.

Final Score: After completing all 10 questions, the application provides the total number of correct answers out of 10.

Setup
Environment Variables: Ensure that your OpenAI API key is set as the environment variable OPENAI_API_KEY. You can obtain your API key from the OpenAI platform.


export OPENAI_API_KEY="your-api-key"
Dependencies Installation: Install the required Python dependencies using the following command:


pip install openai streamlit python-dotenv
Run the Application: Execute the application script using the following command:


streamlit run your_script_name.py
Interact with the Quiz: Access the quiz application through the provided web link after running the script. Answer the questions presented by the assistant and enjoy the quiz experience!

Usage
Upon launching the application, the assistant introduces the quiz format and rules.
Users specify the topic or subject on which they want to be quizzed.
The assistant generates and presents a series of 10 progressively difficult questions.
Users respond to each question, and the correct answers are not immediately revealed.
After completing all questions, the application displays the total number of correct answers out of 10.
Additional Notes
Simulated Typing: The application simulates typing by displaying the assistant's responses with a slight delay, providing a more natural conversational feel.

Message History: The application keeps track of the chat history using Streamlit's session state to maintain continuity between user inputs and assistant responses.

Feel free to explore, learn, and enjoy the quiz experience provided by the AGI Quiz Application!
