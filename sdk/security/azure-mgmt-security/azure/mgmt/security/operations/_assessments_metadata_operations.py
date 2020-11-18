# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AssessmentsMetadataOperations(object):
    """AssessmentsMetadataOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.security.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.SecurityAssessmentMetadataList"]
        """Get metadata information on all assessment types.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityAssessmentMetadataList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.security.models.SecurityAssessmentMetadataList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SecurityAssessmentMetadataList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('SecurityAssessmentMetadataList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/Microsoft.Security/assessmentMetadata'}  # type: ignore

    def get(
        self,
        assessment_metadata_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SecurityAssessmentMetadata"
        """Get metadata information on an assessment type.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
        :type assessment_metadata_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata, or the result of cls(response)
        :rtype: ~azure.mgmt.security.models.SecurityAssessmentMetadata
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SecurityAssessmentMetadata"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'assessmentMetadataName': self._serialize.url("assessment_metadata_name", assessment_metadata_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SecurityAssessmentMetadata', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}'}  # type: ignore

    def list_by_subscription(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.SecurityAssessmentMetadataList"]
        """Get metadata information on all assessment types in a specific subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SecurityAssessmentMetadataList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.security.models.SecurityAssessmentMetadataList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SecurityAssessmentMetadataList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('SecurityAssessmentMetadataList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata'}  # type: ignore

    def get_in_subscription(
        self,
        assessment_metadata_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SecurityAssessmentMetadata"
        """Get metadata information on an assessment type in a specific subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
        :type assessment_metadata_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata, or the result of cls(response)
        :rtype: ~azure.mgmt.security.models.SecurityAssessmentMetadata
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SecurityAssessmentMetadata"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_in_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'assessmentMetadataName': self._serialize.url("assessment_metadata_name", assessment_metadata_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SecurityAssessmentMetadata', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_in_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}'}  # type: ignore

    def create_in_subscription(
        self,
        assessment_metadata_name,  # type: str
        assessment_metadata,  # type: "models.SecurityAssessmentMetadata"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SecurityAssessmentMetadata"
        """Create metadata information on an assessment type in a specific subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
        :type assessment_metadata_name: str
        :param assessment_metadata: AssessmentMetadata object.
        :type assessment_metadata: ~azure.mgmt.security.models.SecurityAssessmentMetadata
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SecurityAssessmentMetadata, or the result of cls(response)
        :rtype: ~azure.mgmt.security.models.SecurityAssessmentMetadata
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SecurityAssessmentMetadata"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_in_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'assessmentMetadataName': self._serialize.url("assessment_metadata_name", assessment_metadata_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(assessment_metadata, 'SecurityAssessmentMetadata')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SecurityAssessmentMetadata', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_in_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}'}  # type: ignore

    def delete_in_subscription(
        self,
        assessment_metadata_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete metadata information on an assessment type in a specific subscription, will cause the
        deletion of all the assessments of that type in that subscription.

        :param assessment_metadata_name: The Assessment Key - Unique key for the assessment type.
        :type assessment_metadata_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-01-01"
        accept = "application/json"

        # Construct URL
        url = self.delete_in_subscription.metadata['url']  # type: ignore
        path_format_arguments = {
            'assessmentMetadataName': self._serialize.url("assessment_metadata_name", assessment_metadata_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_in_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Security/assessmentMetadata/{assessmentMetadataName}'}  # type: ignore
