# perfscale-jupyter-notebooks
Jupyter Notebooks used by the Performance &amp; Scale Organization

This page contains file to automate visualizations using jupyter nootebooks using Touchstone.

There are 2 different fuction that can be called by Touchstone
1) Provides data vast amount of data that is mostly used for calling data with timestamps. This data can not use the aggregate function in the JSON file.
2) Retrives data upto 10k records with aggreation function 



Below is an example of how to use touchstone with jupyter notebooks 

Provide the following details:

uuid="aeed6306-b7e1-11eb-b313-e86a640406b2"
database="elasticsearch"
es_index = "ocm-requests"
es_url="https://search-perfscale-dev-chmf5l4sh66lvxbnadi4bznl3a.us-west-2.es.amazonaws.com"
benchmark = Benchmark(open("ocm-requests.json"), database)

Touchstone (original function call in jupyter):
  This is specified by calling the conn.emit_compute_dict function
  Can create aggregations and filter data through touchstone 
  Limit of 10k records
  Returns nested dictionary
  
  example:
  for compute in benchmark.compute_map['ocm-requests'] :
      conn=databases.grab(database,es_url)
      result=conn.emit_compute_dict(uuid,
                                    compute,
                                    "ocm-requests",
                                    "uuid")
      mergedicts(result,main)
      
      
Touchstone (new function call in jupyter):
  This is specified by calling the database_instance.get_timeserices_results
  Does not have a limit of 10k
  return a dictionary
  JSON file must contain "timeseries": true statement 
  
  example:
  for compute in benchmark.compute_map['ocm-requests'] :
    print("Getting results")
    timeseries_result1 = database_instance.get_timeseries_results(uuid=uuid, 
                                                                 compute_map = compute,
                                                                 index = es_index,
                                                                 identifier="uuid"
                                                                )   
    df = pd.DataFrame(timeseries_result1)



    
    
