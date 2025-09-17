A highly effective prompt for GitHub Copilot follows a two-stage process: a "spec-first" approach. This method has been shown to be far more successful than simply asking for the final code upfront.

Stage 1: The Product Requirements Document (PRD)
Start by prompting Copilot to act as a product manager or game designer. This provides the AI with the necessary context and a clear plan before any code is written.

Prompt:

"Act as a game designer. I want to build a simple, interactive web-based game for a professional event targeted at fintech founders and investors. The game should be a quiz-style challenge that tests knowledge of financial technology concepts like blockchain, AI in finance, and derivatives.

Generate a detailed, Minimal Viable Product (MVP) specification for this game. Include the following sections:

Core Gameplay Loop: Describe the player's journey from start to finish.

Game Rules: Define how players progress, how scores are calculated, and the win condition.

Content Requirements: Propose 5-7 questions that are scenario-based rather than simple trivia. These questions should be related to the following GitHub projects, but framed in a business context:

finAIguard (AI for fraud detection)

onchain-aml-dashboard (on-chain anti-money laundering)

DerivX / blockscholes (derivatives trading)

BlockVista-Terminal (blockchain explorers)

User Interface (UI) Components: List the key screens and elements (e.g., a welcome screen with name input, the quiz screen, a final results page with a shareable image, a button to get a POAP).

Do not write any code yet. Just provide the detailed plan."

Stage 2: The Code Generation
Once Copilot returns the detailed spec, the next step is to use that context to generate the code. This is where you leverage Copilot's ability to act as a "pair programmer."

Prompt:

"Based on the MVP specification you just created, write a complete, self-contained web application. Use a technology stack suitable for a simple, single-page web app.

Stack Requirements:

Frontend: Pure HTML, CSS, and JavaScript. The entire application should be contained within a single index.html file. Do not use any external frameworks like React or Vue.

Functionality:

Implement the core gameplay loop as described in the spec.

The game should handle user name input on a welcome screen.

It should present the questions and options.

It must calculate and display the final score.

The final results page should include a simple, static div that is ready to be screenshotted for social media. This div should clearly display the user's name and final score.

Code Structure:

Use clear comments to explain each function and key part of the logic.

Ensure the code is well-structured and easy to read.

Begin writing the full index.html file now."

<br>
<br>
After you get the initial code, you can use follow-up prompts to refine it. For example:
> "Add a 'Restart Game' button on the results page that reloads the application to the welcome screen."

By providing this structured, two-part prompt, you are using GitHub Copilot not just as a code completion tool, but as a true development partner—guiding it to build a complex application from a high-level idea down to the final implementation.
