def get_demo_dist(df_intern=pd.DataFrame()):
  if df_intern.empty:
    return "Invalid DataFrame"
  tmp_list = []
  for index, row in df_intern.iterrows():
    if (type(row["demographic_distribution"]) is str):
      tup = eval(row["demographic_distribution"])
      if len(tup) > 0:
        if type(tup) is not tuple:
          df_tmp = pd.DataFrame(tup, index=[0]).groupby(by=["age","gender"]).sum().reset_index()
        else:
          df_tmp = pd.DataFrame(tup).groupby(by=["age","gender"]).sum().reset_index()
        tmp_list.append(df_tmp.copy())
  len_ = len(tmp_list)
  df_concat = pd.concat(tmp_list)

  ages = df_concat.age.unique()
  genders = df_concat.gender.unique()
  dict_tmp = {
      "age": [],
      "gender": [],
      "percentage": []
  }
  for a in ages:
    for g in genders:
      dict_tmp["age"].append(a)
      dict_tmp["gender"].append(g)
      dict_tmp["percentage"].append(df_concat[(df_concat["age"] == a) & (df_concat["gender"] == g)].percentage.sum()/len(tmp_list))

  return pd.DataFrame(dict_tmp).copy()
