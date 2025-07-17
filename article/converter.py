import re
from datetime import datetime

# Get today's date
today = datetime.now()
# Format the date
formatted_date = today.strftime("%B %d, %Y")



def main(article_filepath):
    article_fio = open(article_filepath).readlines()    
    title = ""
    h3 = []
    
    for line in article_fio:
        if line.find("\\TITLE") != -1:
            title = re.search(r"\\TITLE\{(.*?)\}", line).group(1)
            break
        
    for line in article_fio:
        if line.find("\\HEAD") != -1:
            h3.append(re.search(r"\\HEAD\{(.*?)\}", line).group(1))
    
    
    # create a table of contents
    h3_id = []
    table_of_contents_html = ""
    
    for header in h3:
        h3_id.append(f"<li><a href=\"#{header.replace(" ", "").lower()}\">{header}</a></li>")
        table_of_contents_html += h3_id[-1]
    
    table_of_contents_html = "<ul>" + table_of_contents_html + "</ul>"
    
    # for each article, encompass each portion
    paragraphs = [""]
    i = 0
    for line in article_fio:
        if line.find("\\HEAD") != -1:
            i += 1
            paragraphs.append("")
            ...
        else:
            paragraphs[i] += line
            ...
    paragraphs = paragraphs[1:]
    
    article_content_html = ""
    for idx in range(len(paragraphs)):
        # get rid of the beginning and end white space
        paragraphs[idx] = f"<h2 id=\"{h3[idx].replace(" ", "").lower()}\">{h3[idx]}</h2><p>" + paragraphs[idx].strip() + "</p>"
        article_content_html += paragraphs[idx]
            
    
    
    template_file = open("article_template.html").readlines()
    template = ""
    for l in template_file:
        template += l
    
    template = template.replace("[ARTICLE TITLE]", title)
    template = template.replace("[DATE]", formatted_date)
    template = template.replace("[TABLE OF CONTENTS]", table_of_contents_html)
    template = template.replace("[ARTICLE]", article_content_html)
    
    
    output_filename = article_filepath.split('.')[0] + ".html"
    print(output_filename)
    
    output_file = open(output_filename, "w")
    output_file.write(template)
    ...




main("custom_ml_lib.article")
