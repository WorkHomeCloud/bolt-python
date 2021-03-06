from logging import Logger
from typing import Optional

from slack_sdk.web import WebClient

from slack_bolt.context.context import BoltContext


class AuthorizeArgs:
    context: BoltContext
    logger: Logger
    client: WebClient
    enterprise_id: Optional[str]
    team_id: str
    user_id: Optional[str]

    def __init__(
        self,
        *,
        context: BoltContext,
        enterprise_id: Optional[str],
        team_id: str,
        user_id: Optional[str],
    ):
        """The whole arguments that are passed to Authorize functions.

        :param context: The request context
        :param enterprise_id: The Organization ID (Enterprise Grid)
        :param team_id: The workspace ID
        :param user_id: The request user ID
        """
        self.context = context
        self.logger = context.logger
        self.client = context.client
        self.enterprise_id = enterprise_id
        self.team_id = team_id
        self.user_id = user_id
