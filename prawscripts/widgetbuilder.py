def widgetbuilder(instance, sub_name, widget_title, background_color, header_color, subList):
    """
    Simple script that that runs a PRAW instance and build a community widget.
    
    Parameters
    ----------
    instance : PRAW Reddit Object
        The name of the PRAW instance
    sub_name : str
        The name of the sub-reddit you're working on
    widget_title : str
        The title of your widget
    background_color : str
        Background color for your widget using hex formatted color
    header_color : str
        Header color for your widget using hex formatted color
    subList : list
        List of related subreddits communities

    Returns
    -------
    new_widget
        The newly created community widget
    """
    widget_moderation = instance.subreddit(sub_name).widget.widget_mod
    styles = {"backgroundColor", background_color, "headerColor", header_color}
    subreddits = subList
    new_widget = widget_moderation.add_communit_list(widget_title, subreddits, styles)

    return new_widget