def get_demo_dist(df_intern=pd.DataFrame()):
  if df_intern.empty:
    return "Invalid DataFrame"
  tmp_list = []
  for index, row in df_intern.iterrows():
    if (type(row['delivery_by_region']) is str):
      tup = eval(row['delivery_by_region'])
      if len(tup) > 0:
        if type(tup) is not tuple:
          df_tmp = pd.DataFrame(tup, index=[0]).groupby(by=["region"]).sum().reset_index()
        else:
          df_tmp = pd.DataFrame(tup).groupby(by=["region"]).sum().reset_index()
        tmp_list.append(df_tmp.copy())
  len_ = len(tmp_list)
  df_concat = pd.concat(tmp_list)

  regions = df_concat.region.unique()
  dict_tmp = {
      "region": [],
      "percentage": []
  }
  for r in regions:
    dict_tmp["region"].append(r)
    dict_tmp["percentage"].append(df_concat[(df_concat["region"] == r)].percentage.sum()/len(tmp_list))

  return pd.DataFrame(dict_tmp).copy()
