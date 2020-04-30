def _render(template, context, app):
    """Renders the template and fires the signal"""

    before_render_template.send(app, template=template, context=context)
    rv = template.render(context)
    template_rendered.send(app, template=template, context=context)
    return rv

