"""
Django Ledger created by Miguel Sanda <msanda@arrobalytics.com>.
Modified to send feedback directly to GitHub Issues.
"""

import os
import requests

from django.views.generic import FormView
from django_ledger.forms.feedback import BugReportForm, RequestNewFeatureForm
from django_ledger.views.mixins import DjangoLedgerSecurityMixIn, SuccessUrlNextMixIn


# GitHub configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = "Deekshithmmm/Double-entry-ledger"


def create_github_issue(title, body):

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "title": title,
        "body": body
    }

    response = requests.post(url, headers=headers, json=payload)

    return response


class BugReportView(DjangoLedgerSecurityMixIn,
                    SuccessUrlNextMixIn,
                    FormView):

    http_method_names = ['post']
    form_class = BugReportForm

    def form_valid(self, form):

        form_data = form.cleaned_data

        message = (
            f"### Bug Report\n\n"
            f"How to reproduce:\n{form_data['reproduce']}\n\n"
            f"Expected behavior:\n{form_data['expectation']}\n\n"
            f"Device:\n{form_data['device']}\n\n"
            f"User: {self.request.user.username}\n"
            f"Email: {self.request.user.email}"
        )

        create_github_issue(
            title="Bug Report from Website",
            body=message
        )

        return super().form_valid(form)


class RequestNewFeatureView(DjangoLedgerSecurityMixIn,
                            SuccessUrlNextMixIn,
                            FormView):

    http_method_names = ['post']
    form_class = RequestNewFeatureForm

    def form_valid(self, form):

        form_data = form.cleaned_data

        message = (
            f"### Feature Request\n\n"
            f"Description:\n{form_data['feature_description']}\n\n"
            f"Solution:\n{form_data['solution']}\n\n"
            f"Alternatives:\n{form_data['alternatives']}\n\n"
            f"User: {self.request.user.username}\n"
            f"Email: {self.request.user.email}"
        )

        create_github_issue(
            title="Feature Request from Website",
            body=message
        )

        return super().form_valid(form)