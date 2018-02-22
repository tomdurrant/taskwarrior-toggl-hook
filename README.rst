taskwarrior toggl Hook
=========================

Requirements
------------

Install and configure `toggl-cli <https://github.com/drobertadams/toggl-cli>`_. Add main command to your path as toggl

Install 
--------

And add this it to your Taskwarrior hooks::

    mkdir -p ~/.task/hooks
    ln -s on-modify.toggl ~/.task/hooks/on-modify.toggl

Usage 
--------

Use ``task <TASK ID> start`` and ``task <TASK ID> stop`` to record when you have
started and stopped working on tasks.

Tasks will appear in your `toggl <https://toggl.com/>`_ automatically.
