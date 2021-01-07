from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from presentation.models import *  # import all models

def index(request):
    id_names = Topics.objects.values('id', 'name')  # list of dicts


    return HttpResponse("Hello word. This is a test view for the presentation app")

def summary_view(request, tech_slug, inst_id, topic_id):
    # tech_name, inst_id, topic_name, summary_instance
    tech_name = technique_name(tech_slug)
    meta = InstanceMeta.objects.get(topic=topic_id, instance=inst_id)
    topic_title = meta.topic.title
    summary = meta.summary

    context = {"tech_name":tech_name, "inst_id":inst_id, "topic_title":topic_title, "summary_instance":summary}
    return render(request, 'summary.html', context)

def topic_view(request, tech_slug, inst_id):
    topic_metas = InstanceMeta.objects.filter(instance=int(inst_id))

    topic_list = []
    for topic_meta in topic_metas:
        t = topic_meta.topic
        # t_name = Topics.objects.filter(topic_id=t_id).name
        t = {"id":t.topic_id, "title":t.title}
        topic_list.append(t)

    context = {"topic_list":topic_list, "tech_slug":tech_slug, "inst_id":inst_id}
    return render(request, "topics.html", context)

def instance_view(request, tech_slug):
    instances = Instances.objects.filter(technique=technique_name(tech_slug))
    context = {"instances_list":instances, "technique":tech_slug}
    return render(request, 'instances.html', context)



def technique_view(request):

    techniques = Techniques.objects.all()
    context = {"technique_list":techniques}
    return render(request, 'techniques.html', context)


def technique_name(tech_slug):
    technique = Techniques.objects.get(slug=tech_slug)
    return technique.name

    # technique_list = Techniques.objects.values('name')

    # button_list = []
    # for technique in technique_list:
    #     # get url
    #     url = "https://ddg.gg"  # change to url to show technique's instances
    #     button = {"name":technique['name'], "url":url}
    #     button_list.append(button)
    #     # 'instance_view' && 'technique.slug'

    # techniques = Techniques.objects.all()
    # button_list = []
    # for technique in techniques:
    #     name = technique.name
    #     view = 'instance_view'
    #     button = {"name":name, "technique":technique}
    #     button_list.append(button)
    
    # context = {"button_list":button_list}
    # return render(request, 'techniques.html', context)


