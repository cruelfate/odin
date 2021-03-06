# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.pipeline_cleanup_definition import PipelineCleanupDefinition  # noqa: F401,E501
from swagger_server import util


class PipelineCleanupResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cleanups: List[PipelineCleanupDefinition]=None):  # noqa: E501
        """PipelineCleanupResults - a model defined in Swagger

        :param cleanups: The cleanups of this PipelineCleanupResults.  # noqa: E501
        :type cleanups: List[PipelineCleanupDefinition]
        """
        self.swagger_types = {
            'cleanups': List[PipelineCleanupDefinition]
        }

        self.attribute_map = {
            'cleanups': 'cleanups'
        }
        self._cleanups = cleanups

    @classmethod
    def from_dict(cls, dikt) -> 'PipelineCleanupResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PipelineCleanupResults of this PipelineCleanupResults.  # noqa: E501
        :rtype: PipelineCleanupResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cleanups(self) -> List[PipelineCleanupDefinition]:
        """Gets the cleanups of this PipelineCleanupResults.


        :return: The cleanups of this PipelineCleanupResults.
        :rtype: List[PipelineCleanupDefinition]
        """
        return self._cleanups

    @cleanups.setter
    def cleanups(self, cleanups: List[PipelineCleanupDefinition]):
        """Sets the cleanups of this PipelineCleanupResults.


        :param cleanups: The cleanups of this PipelineCleanupResults.
        :type cleanups: List[PipelineCleanupDefinition]
        """

        self._cleanups = cleanups
