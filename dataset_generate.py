import json
import random

# Your sentence templates
prompt_templates = [
    "\nUser: I'm at a loss regarding what I should study to gain knowledge about the {concept}.\nAI:",
    "\nUser: Where should I begin in order to grasp the fundamentals of {concept}?\nAI:",
    "\nUser: I have a desire to explore the {concept}, but I'm uncertain about the initial steps I should take.\nAI:",
    "\nUser: What foundational knowledge do I need to acquire before embarking on the study of {concept}?\nAI:",
    "\nUser: I'm interested in delving into the {concept} , but I'm unsure of how to get started.\nAI:",
    "\nUser: I have a strong inclination to pursue a deep understanding of the {concept}, yet I find myself unsure of how to initiate my journey.\nAI:",
    "\nUser: The {concept} captivates my interest, but I find myself lacking guidance on where to commence my study.\nAI:",
    "\nUser: I yearn to delve into the intricacies of the {concept}, but I'm perplexed as to how I should commence my educational pursuit.\nAI:",
    "\nUser: The vast realm of {concept} beckons me, but I feel disoriented about how to embark on my quest for knowledge.\nAI:",
    "\nUser: I'm eager to immerse myself in the study of the {concept}, but I'm struggling to ascertain the ideal starting point.\nAI:",
    "\nUser: I'm captivated by the idea of understanding the {concept}, yet I'm unsure where to begin my exploration.\nAI:",
    "\nUser: I'm intrigued by the {concept} and want to learn more about it, but I don't know where to start.\nAI:",
    "\nUser: I'm fascinated by the {concept} but need advice on the preliminary steps to studying it.\nAI:",
    "\nUser: I have a burgeoning interest in the {concept}, but I am uncertain about the ideal initial learning steps.\nAI:",
    "\nUser: I'm enthusiastic about gaining a deeper understanding of the {concept}, but the starting point seems elusive.\nAI:",
    "\nUser: The {concept} intrigues me, yet I'm in need of guidance to embark on this educational journey.\nAI:",
    "\nUser: I find the {concept} compelling and want to study it, yet I'm unsure of the most effective way to initiate my learning.\nAI:",
    "\nUser: I aspire to master the {concept}, but I'm uncertain about how to lay the groundwork.\nAI:",
    "\nUser: The {concept} has piqued my curiosity, but I could use some advice on where to start my study.\nAI:",
    "\nUser: I'm keen to delve deeper into the {concept}, but I'm unsure of the foundational knowledge required to commence my studies.\nAI:",
    "\nUser: I'm motivated to deepen my understanding of the {concept}, but I'm unsure about the best starting point.\nAI:",
    "\nUser: The {concept} is a topic I'd love to explore, but I need some guidance on how to begin.\nAI:",
    "\nUser: I'm interested in diving into the {concept}, but I'm uncertain about where to kick-start my learning.\nAI:",
    "\nUser: The {concept} is something I'd like to master, but I need advice on how to start this journey.\nAI:",
    "\nUser: I have a burning curiosity about the {concept}, but I'm unsure about how to commence my studies.\nAI:",
    "\nUser: I'm excited about acquiring a comprehensive knowledge of the {concept}, but I'm unsure about where to initiate my learning.\nAI:",
    "\nUser: The {concept} sparks my curiosity, but I need some directions to start my exploration.\nAI:",
    "\nUser: I want to gain a solid grasp of the {concept}, but I'm uncertain about the most effective starting point.\nAI:",
    "\nUser: The {concept} appeals to me greatly, but I'm at a loss for where to start my education journey.\nAI:",
    "\nUser: I wish to delve deeply into the {concept}, but I'm uncertain about how to set the stage for this learning endeavor.\nAI:"
]

completion_templates = [
    " To properly grasp the intricacies of the {concept}, it is advisable to study {another_concept} as a prerequisite.\n",
    " Before embarking on your study of {concept}, it would be beneficial to familiarize yourself with {another_concept} first.\n",
    " Considering your interest in {concept}, it would be advantageous to acquire foundational knowledge in {another_concept} beforehand.\n",
    " To effectively comprehend the nuances of {concept}, it is recommended to begin by studying {another_concept}.\n",
    " Prior to diving into the study of {concept}, it would be prudent to gain a solid understanding of {another_concept}.\n",
    " In order to build a solid foundation for your exploration of the {concept}, it is essential to prioritize studying {another_concept}.\n",
    " To enhance your comprehension of {concept}, it is crucial to lay the groundwork by delving into the realm of {another_concept}.\n",
    " Before delving into the depths of {concept}, I suggest immersing yourself in the knowledge of {another_concept}.\n",
    " To ensure a comprehensive understanding of {concept}, it is highly recommended to dedicate time to studying {another_concept} beforehand.\n",
    " Maximizing your understanding of {concept} necessitates familiarizing yourself with the fundamentals of {another_concept} beforehand.\n",
    " To fully grasp the {concept}, it would be helpful to have a grounding in {another_concept} initially.\n",
    " It's recommended to have a basic understanding of {another_concept} before you dive into studying the {concept}.\n",
    " To make the most out of your study of {concept}, it would be beneficial to first have a solid foundation in {another_concept}.\n",
    " A study of {another_concept} will provide a beneficial basis before starting to learn about the {concept}.\n",
    " Having a preliminary understanding of {another_concept} will significantly enhance your comprehension of the {concept}.\n",
    " A good starting point for delving into the {concept} would be to study {another_concept} first.\n",
    " For a robust understanding of {concept}, it's vital to first establish a foundation in {another_concept}.\n",
    " To start off your learning journey for the {concept}, it's suggested to first understand the basics of {another_concept}.\n",
    " Understanding {another_concept} can pave the way for a deeper comprehension of the {concept}.\n",
    " Prior to exploring the complex world of {concept}, gaining a robust understanding of {another_concept} can be really helpful.\n",
    " To unravel the mysteries of the {concept}, it's beneficial to first get acquainted with {another_concept}.\n",
    " Embarking on a journey to understand {concept} is smoother when equipped with a prior knowledge of {another_concept}.\n",
    " It's wise to ground yourself in the understanding of {another_concept} before attempting to learn the {concept}.\n",
    " Familiarity with {another_concept} can be a stepping stone towards a successful comprehension of the {concept}.\n",
    " Before taking a deep dive into {concept}, it's suggested to first navigate the waters of {another_concept}.\n",
    " Understanding {another_concept} could act as a catalyst to your exploration of the {concept}.\n",
    " A solid grasp of {another_concept} can act as a primer for a better understanding of the {concept}.\n",
    " To successfully conquer the realm of {concept}, it's beneficial to first lay a solid foundation in {another_concept}.\n",
    " Before venturing into the intricacies of the {concept}, it's advisable to first explore the domain of {another_concept}.\n",
    " Diving into the {concept} can be made easier by first gaining proficiency in {another_concept}.\n"
]

# Function to format a prompt and completion
def create_prompt_and_completion(concept1, concept2):
    prompt = random.choice(prompt_templates).format(concept=concept1)
    completion = random.choice(completion_templates).format(concept=concept1, another_concept=concept2)
    return {"prompt": prompt, "completion": completion}

# Read the input file and generate prompts and completions
with open("ML_LabeledFile", 'r') as infile, open("dataset_ML.jsonl", 'w') as outfile:
    for line in infile:
        line = line.replace("    ", "\t").strip()  # replace 4 spaces with a tab character and remove newline characters
        concept1, concept2, label = line.split('\t')  # split the line into parts

        if label == '1-':  # concept2 is a prerequisite of concept1
            pc = create_prompt_and_completion(concept1, concept2)
            json.dump(pc, outfile)
            outfile.write("\n")
        elif label == '-1':  # concept1 is a prerequisite of concept2
            pc = create_prompt_and_completion(concept2, concept1)
            json.dump(pc, outfile)
            outfile.write("\n")
