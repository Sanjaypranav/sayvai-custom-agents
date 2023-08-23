# Pytest to test import 
    
def test_import():
    from agents.customagents.human import CustomHumanAgent
    from agents.customprompt.prompt import CustomPromptTemplate
    from agents.parser.parser import CustomOutputParser
    from agents.templates import template, template_with_history
    assert True