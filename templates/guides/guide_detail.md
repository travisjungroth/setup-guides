# {{ guide.title }}
{% for step in guide.steps.all %}
## {{ step.title }}{% if guide_step.optional %} (optional){% endif %}
{% if step.requirements.exists %}
### Requirements
{% for requirement in step.requirements.all %}
 - {{ requirement.title }}
{% endfor %}
{% endif %}
### Actions
{% for action in step.actions.all %}
{{ forloop.counter }}. {{ action.text}}
{% endfor %}
### Verifications
{% for verification in step.verifications.all %}
{{ verification.text }}
{% endfor %}
{% endfor %}
