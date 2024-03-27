

import openai
openai.api_key = ""

def generrate_answer(qs):

        
    panswer = ""
    
    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": ""},
                            {"role": "user", "content": f": {data}"},
                                ],
                                    )
    txt_translate = response["choices"][0]["message"]["content"]
    answer += txt_translate + "\n"

    return answer


def convert(value):
        return value.replace('_', ' ').title()

def generate_string(project1, project2):
   
  
    result_string = ""
    
    for field in project1._meta.fields:
            
            column_name = convert(field.name)
            if column_name == 'Id' or column_name == 'User':
                    continue
            column_value = getattr(project1, field.name)
            result_string += f"{column_name}: {column_value}\n"
            
    for field in project2._meta.fields:
            column_name = convert(field.name)
            
            if column_name == 'Id' or column_name == 'User':
                    continue
            column_value = getattr(project2, field.name)
            result_string += f"{column_name}: {column_value}\n"

    return generrate_answer(result_string)






        
