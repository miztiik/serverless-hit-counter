#!/usr/bin/env python3

from aws_cdk import core

from serverless_hit_counter.serverless_hit_counter_stack import ServerlessHitCounterStack


app = core.App()
ServerlessHitCounterStack(app, "serverless-hit-counter")

app.synth()
