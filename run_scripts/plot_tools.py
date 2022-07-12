import matplotlib.pyplot as plt
import seaborn as sns




def plot_one_column(df,col_name,save_path):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    plt.plot(df[col_name], label=col_name)
    plt.legend()
    plt.savefig(save_path)
    
def plot_one_column_with_label(df,col_name, anomal_col, save_path):
    a = df.loc[df[anomal_col] == 1]
    outlier_index=list(a.index)
    fig = plt.figure(facecolor='white')
    
    ax = fig.add_subplot(111)
    plt.plot(df[col_name], label=col_name)
    ax.scatter(a.index ,a[col_name], color='red', label = 'Anomaly', s=16)
    plt.legend()
    plt.savefig(save_path)
    
def plot_one_column_with_label_and_predict(df,col_name, anomal_col, pred_series, save_path):
    pass
 
def plot_one_column_dense(df,col_name,save_path):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    sns.kdeplot(df[col_name],label=col_name)
    plt.legend()
    plt.savefig(save_path)

def plot_predict(df,col_name,anomal_col,predict,save_path):
    a = df.loc[df[anomal_col] == 1]
    outlier_index=list(a.index)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df[col_name], color='black', label = 'Normal', linewidth=1.5)
    ax.scatter(a.index ,a[anomal_col], color='red', label = 'Anomaly', s=16)
    ax.plot(predict, color='blue', label = 'Score', linewidth=0.5)
    plt.savefig(save_path)
    
    
    

def plot_multi_columns(df,col_names,save_path):
    fig = plt.figure(facecolor='white')
    ax = fig.add_subplot(111)
    for col_name in col_names:
        plt.plot(df[col_name], label=col_name)
    plt.legend(col_names,title='multi columns')
    plt.savefig(save_path)
    

    
    
def plot_anomal_multi_columns(df, col_names, anomal_col,save_path):
    a = df.loc[df[anomal_col] == 1]
    outlier_index=list(a.index)
    print("outlier_index: ",outlier_index)
    fig, ax = plt.subplots(figsize=(10,6))   
    for col_name in col_names:
        ax.plot(df[col_name], label=col_name)
    for col_name in col_names:
        ax.scatter(a.index ,a[col_name], color='red',label="anomaly", s=16)
    plt.legend(col_names)
    plt.savefig(save_path)
    

def plot_anomal_multi_columns_3d(df,col_names, anomal_col,save_path):
    assert len(col_names) <= 3 ,"too many cols for 3d plot"
    a = df.loc[df[anomal_col] == 1]
    outlier_index=list(a.index)
    print("outlier_index: ",outlier_index)
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    #ax.set_zlabel("x_composite_3")
    ax.scatter(df[col_names[0]], df[col_names[1]], zs=df[col_names[2]], s=5, lw=1, label="inliers", c="blue")
    # Plot x's for the ground truth outliers
    ax.scatter(df.loc[outlier_index,col_names[0]],df.loc[outlier_index,col_names[1]], df.loc[outlier_index,col_names[2]],
            lw=1, s=15, c="red", label="outliers")
    ax.legend()
    plt.title("Anamoly Detection Using DeepLog")
    plt.savefig(save_path)
    