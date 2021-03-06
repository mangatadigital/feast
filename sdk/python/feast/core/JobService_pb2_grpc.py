# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from feast.core import JobService_pb2 as feast_dot_core_dot_JobService__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class JobServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubmitJob = channel.unary_unary(
        '/feast.core.JobService/SubmitJob',
        request_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.SubmitImportJobRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.SubmitImportJobResponse.FromString,
        )
    self.ListJobs = channel.unary_unary(
        '/feast.core.JobService/ListJobs',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.ListJobsResponse.FromString,
        )
    self.GetJob = channel.unary_unary(
        '/feast.core.JobService/GetJob',
        request_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.GetJobRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.GetJobResponse.FromString,
        )
    self.AbortJob = channel.unary_unary(
        '/feast.core.JobService/AbortJob',
        request_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.AbortJobRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.AbortJobResponse.FromString,
        )


class JobServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SubmitJob(self, request, context):
    """Submit a job to feast to run. Returns the job id.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListJobs(self, request, context):
    """List all jobs submitted to feast.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetJob(self, request, context):
    """Get Job with ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AbortJob(self, request, context):
    """Abort job with given ID
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubmitJob': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitJob,
          request_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.SubmitImportJobRequest.FromString,
          response_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.SubmitImportJobResponse.SerializeToString,
      ),
      'ListJobs': grpc.unary_unary_rpc_method_handler(
          servicer.ListJobs,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.ListJobsResponse.SerializeToString,
      ),
      'GetJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetJob,
          request_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.GetJobRequest.FromString,
          response_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.GetJobResponse.SerializeToString,
      ),
      'AbortJob': grpc.unary_unary_rpc_method_handler(
          servicer.AbortJob,
          request_deserializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.AbortJobRequest.FromString,
          response_serializer=feast_dot_core_dot_JobService__pb2.JobServiceTypes.AbortJobResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'feast.core.JobService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
