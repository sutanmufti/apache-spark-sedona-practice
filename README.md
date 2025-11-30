# Apache Sedona Cluster Practice

Let's practice Apache Sedona for distributed spatial data analysis.

Data source:

[Riyadh places](https://source.coop/tabaqat/riyadh-places/riyadh_places.parquet)

Download

```bash
curl -o ./shared/riyadh_places.parquet https://data.source.coop/tabaqat/riyadh-places/riyadh_places.parquet
```


Example of submitting the spark job:

[spark_submit.sh](./spark_submit.sh)


# Setup

install docker and docker compose. Run the "cluster".

```bash
docker compose up -d
```

edit the [`./jobs/job.py`](./jobs/job.py). Do the code.

submit the job

```
docker exec -it \
  sedona-master \
  /opt/spark/bin/spark-submit \
    --master spark://sedona-master:7077 \
    /jobs/job.py
```


example of the following:

```bash
docker exec -it \
  sedona-master \
  /opt/spark/bin/spark-submit \
    --master spark://sedona-master:7077 \
    /jobs/sample-job.py
```

outputs:

```
25/11/30 04:41:16 INFO SparkContext: Running Spark version 3.5.5
25/11/30 04:41:16 INFO SparkContext: OS info Linux, 6.10.14-linuxkit, aarch64
25/11/30 04:41:16 INFO SparkContext: Java version 19.0.2
25/11/30 04:41:16 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
25/11/30 04:41:16 INFO ResourceUtils: ==============================================================
25/11/30 04:41:16 INFO ResourceUtils: No custom resources configured for spark.driver.
25/11/30 04:41:16 INFO ResourceUtils: ==============================================================
25/11/30 04:41:16 INFO SparkContext: Submitted application: Sedona Example
25/11/30 04:41:16 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
25/11/30 04:41:16 INFO ResourceProfile: Limiting resource is cpu
25/11/30 04:41:16 INFO ResourceProfileManager: Added ResourceProfile id: 0
25/11/30 04:41:16 INFO SecurityManager: Changing view acls to: root
25/11/30 04:41:16 INFO SecurityManager: Changing modify acls to: root
25/11/30 04:41:16 INFO SecurityManager: Changing view acls groups to: 
25/11/30 04:41:16 INFO SecurityManager: Changing modify acls groups to: 
25/11/30 04:41:16 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: root; groups with view permissions: EMPTY; users with modify permissions: root; groups with modify permissions: EMPTY
25/11/30 04:41:16 INFO Utils: Successfully started service 'sparkDriver' on port 46281.
25/11/30 04:41:16 INFO SparkEnv: Registering MapOutputTracker
25/11/30 04:41:16 INFO SparkEnv: Registering BlockManagerMaster
25/11/30 04:41:16 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
25/11/30 04:41:16 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
25/11/30 04:41:16 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
25/11/30 04:41:16 INFO DiskBlockManager: Created local directory at /tmp/blockmgr-304a5476-1d41-4ef4-865f-0cc1bccf3b5b
25/11/30 04:41:16 INFO MemoryStore: MemoryStore started with capacity 434.4 MiB
25/11/30 04:41:16 INFO SparkEnv: Registering OutputCommitCoordinator
25/11/30 04:41:16 INFO JettyUtils: Start Jetty 0.0.0.0:4040 for SparkUI
25/11/30 04:41:16 INFO Utils: Successfully started service 'SparkUI' on port 4040.
25/11/30 04:41:16 INFO StandaloneAppClient$ClientEndpoint: Connecting to master spark://sedona-master:7077...
25/11/30 04:41:16 INFO TransportClientFactory: Successfully created connection to sedona-master/172.20.0.2:7077 after 8 ms (0 ms spent in bootstraps)
25/11/30 04:41:17 INFO StandaloneSchedulerBackend: Connected to Spark cluster with app ID app-20251130044116-0008
25/11/30 04:41:17 INFO StandaloneAppClient$ClientEndpoint: Executor added: app-20251130044116-0008/0 on worker-20251130041015-172.20.0.3-33479 (172.20.0.3:33479) with 4 core(s)
25/11/30 04:41:17 INFO StandaloneSchedulerBackend: Granted executor ID app-20251130044116-0008/0 on hostPort 172.20.0.3:33479 with 4 core(s), 1024.0 MiB RAM
25/11/30 04:41:17 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 35565.
25/11/30 04:41:17 INFO NettyBlockTransferService: Server created on 9515d4ca2c5d:35565
25/11/30 04:41:17 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
25/11/30 04:41:17 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, 9515d4ca2c5d, 35565, None)
25/11/30 04:41:17 INFO BlockManagerMasterEndpoint: Registering block manager 9515d4ca2c5d:35565 with 434.4 MiB RAM, BlockManagerId(driver, 9515d4ca2c5d, 35565, None)
25/11/30 04:41:17 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, 9515d4ca2c5d, 35565, None)
25/11/30 04:41:17 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, 9515d4ca2c5d, 35565, None)
25/11/30 04:41:17 INFO StandaloneAppClient$ClientEndpoint: Executor updated: app-20251130044116-0008/0 is now RUNNING
25/11/30 04:41:17 INFO StandaloneSchedulerBackend: SchedulerBackend is ready for scheduling beginning after reached minRegisteredResourcesRatio: 0.0
THE SPARK VERSION IS::: 3.5.5
25/11/30 04:41:17 INFO SharedState: Setting hive.metastore.warehouse.dir ('null') to the value of spark.sql.warehouse.dir.
25/11/30 04:41:17 INFO SharedState: Warehouse path is 'file:/opt/workspace/spark-warehouse'.
25/11/30 04:41:17 INFO InMemoryFileIndex: It took 14 ms to list leaf files for 1 paths.
25/11/30 04:41:17 INFO SparkContext: Starting job: parquet at NativeMethodAccessorImpl.java:0
25/11/30 04:41:17 INFO DAGScheduler: Got job 0 (parquet at NativeMethodAccessorImpl.java:0) with 1 output partitions
25/11/30 04:41:17 INFO DAGScheduler: Final stage: ResultStage 0 (parquet at NativeMethodAccessorImpl.java:0)
25/11/30 04:41:17 INFO DAGScheduler: Parents of final stage: List()
25/11/30 04:41:17 INFO DAGScheduler: Missing parents: List()
25/11/30 04:41:17 INFO DAGScheduler: Submitting ResultStage 0 (MapPartitionsRDD[1] at parquet at NativeMethodAccessorImpl.java:0), which has no missing parents
25/11/30 04:41:17 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 103.6 KiB, free 434.3 MiB)
25/11/30 04:41:17 INFO SedonaKryoRegistrator: Registering custom serializers for geometry types
25/11/30 04:41:17 INFO SedonaVizKryoRegistrator: Registering custom serializers for visualization related types
25/11/30 04:41:17 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 37.4 KiB, free 434.3 MiB)
25/11/30 04:41:17 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on 9515d4ca2c5d:35565 (size: 37.4 KiB, free: 434.4 MiB)
25/11/30 04:41:17 INFO SparkContext: Created broadcast 0 from broadcast at DAGScheduler.scala:1585
25/11/30 04:41:17 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 0 (MapPartitionsRDD[1] at parquet at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
25/11/30 04:41:17 INFO TaskSchedulerImpl: Adding task set 0.0 with 1 tasks resource profile 0
25/11/30 04:41:18 INFO StandaloneSchedulerBackend$StandaloneDriverEndpoint: Registered executor NettyRpcEndpointRef(spark-client://Executor) (172.20.0.3:34590) with ID 0,  ResourceProfileId 0
25/11/30 04:41:18 INFO BlockManagerMasterEndpoint: Registering block manager 172.20.0.3:42151 with 434.4 MiB RAM, BlockManagerId(0, 172.20.0.3, 42151, None)
25/11/30 04:41:18 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0) (172.20.0.3, executor 0, partition 0, PROCESS_LOCAL, 8928 bytes) 
25/11/30 04:41:18 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on 172.20.0.3:42151 (size: 37.4 KiB, free: 434.4 MiB)
25/11/30 04:41:18 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 501 ms on 172.20.0.3 (executor 0) (1/1)
25/11/30 04:41:18 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
25/11/30 04:41:18 INFO DAGScheduler: ResultStage 0 (parquet at NativeMethodAccessorImpl.java:0) finished in 0.937 s
25/11/30 04:41:18 INFO DAGScheduler: Job 0 is finished. Cancelling potential speculative or zombie tasks for this job
25/11/30 04:41:18 INFO TaskSchedulerImpl: Killing all running tasks in stage 0: Stage finished
25/11/30 04:41:18 INFO DAGScheduler: Job 0 finished: parquet at NativeMethodAccessorImpl.java:0, took 0.964003 s
25/11/30 04:41:18 INFO BlockManagerInfo: Removed broadcast_0_piece0 on 9515d4ca2c5d:35565 in memory (size: 37.4 KiB, free: 434.4 MiB)
25/11/30 04:41:18 INFO BlockManagerInfo: Removed broadcast_0_piece0 on 172.20.0.3:42151 in memory (size: 37.4 KiB, free: 434.4 MiB)
25/11/30 04:41:20 INFO CodeGenerator: Code generated in 71.018958 ms
25/11/30 04:41:20 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
25/11/30 04:41:20 INFO DAGScheduler: Got job 1 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
25/11/30 04:41:20 INFO DAGScheduler: Final stage: ResultStage 1 (showString at NativeMethodAccessorImpl.java:0)
25/11/30 04:41:20 INFO DAGScheduler: Parents of final stage: List()
25/11/30 04:41:20 INFO DAGScheduler: Missing parents: List()
25/11/30 04:41:20 INFO DAGScheduler: Submitting ResultStage 1 (MapPartitionsRDD[4] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
25/11/30 04:41:20 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 7.5 KiB, free 434.4 MiB)
25/11/30 04:41:20 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 3.8 KiB, free 434.4 MiB)
25/11/30 04:41:20 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on 9515d4ca2c5d:35565 (size: 3.8 KiB, free: 434.4 MiB)
25/11/30 04:41:20 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:1585
25/11/30 04:41:20 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 1 (MapPartitionsRDD[4] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
25/11/30 04:41:20 INFO TaskSchedulerImpl: Adding task set 1.0 with 1 tasks resource profile 0
25/11/30 04:41:20 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 1) (172.20.0.3, executor 0, partition 0, PROCESS_LOCAL, 8949 bytes) 
25/11/30 04:41:20 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on 172.20.0.3:42151 (size: 3.8 KiB, free: 434.4 MiB)
25/11/30 04:41:20 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 1) in 158 ms on 172.20.0.3 (executor 0) (1/1)
25/11/30 04:41:20 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
25/11/30 04:41:20 INFO DAGScheduler: ResultStage 1 (showString at NativeMethodAccessorImpl.java:0) finished in 0.172 s
25/11/30 04:41:20 INFO DAGScheduler: Job 1 is finished. Cancelling potential speculative or zombie tasks for this job
25/11/30 04:41:20 INFO TaskSchedulerImpl: Killing all running tasks in stage 1: Stage finished
25/11/30 04:41:20 INFO DAGScheduler: Job 1 finished: showString at NativeMethodAccessorImpl.java:0, took 0.175287 s
25/11/30 04:41:20 INFO CodeGenerator: Code generated in 9.920583 ms
+--------------+
|st_point(1, 1)|
+--------------+
|   POINT (1 1)|
+--------------+

25/11/30 04:41:20 INFO FileSourceStrategy: Pushed Filters: 
25/11/30 04:41:20 INFO FileSourceStrategy: Post-Scan Filters: 
25/11/30 04:41:20 INFO CodeGenerator: Code generated in 7.276708 ms
25/11/30 04:41:20 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 201.6 KiB, free 434.2 MiB)
25/11/30 04:41:20 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 35.1 KiB, free 434.2 MiB)
25/11/30 04:41:20 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on 9515d4ca2c5d:35565 (size: 35.1 KiB, free: 434.4 MiB)
25/11/30 04:41:20 INFO SparkContext: Created broadcast 2 from showString at NativeMethodAccessorImpl.java:0
25/11/30 04:41:20 INFO FileSourceScanExec: Planning scan with bin packing, max size: 4194304 bytes, open cost is considered as scanning 4194304 bytes.
25/11/30 04:41:20 INFO SparkContext: Starting job: showString at NativeMethodAccessorImpl.java:0
25/11/30 04:41:20 INFO DAGScheduler: Got job 2 (showString at NativeMethodAccessorImpl.java:0) with 1 output partitions
25/11/30 04:41:20 INFO DAGScheduler: Final stage: ResultStage 2 (showString at NativeMethodAccessorImpl.java:0)
25/11/30 04:41:20 INFO DAGScheduler: Parents of final stage: List()
25/11/30 04:41:20 INFO DAGScheduler: Missing parents: List()
25/11/30 04:41:20 INFO DAGScheduler: Submitting ResultStage 2 (MapPartitionsRDD[9] at showString at NativeMethodAccessorImpl.java:0), which has no missing parents
25/11/30 04:41:20 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 25.8 KiB, free 434.1 MiB)
25/11/30 04:41:20 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 11.3 KiB, free 434.1 MiB)
25/11/30 04:41:20 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on 9515d4ca2c5d:35565 (size: 11.3 KiB, free: 434.4 MiB)
25/11/30 04:41:20 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:1585
25/11/30 04:41:20 INFO DAGScheduler: Submitting 1 missing tasks from ResultStage 2 (MapPartitionsRDD[9] at showString at NativeMethodAccessorImpl.java:0) (first 15 tasks are for partitions Vector(0))
25/11/30 04:41:20 INFO TaskSchedulerImpl: Adding task set 2.0 with 1 tasks resource profile 0
25/11/30 04:41:20 INFO TaskSetManager: Starting task 0.0 in stage 2.0 (TID 2) (172.20.0.3, executor 0, partition 0, PROCESS_LOCAL, 9602 bytes) 
25/11/30 04:41:20 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on 172.20.0.3:42151 (size: 11.3 KiB, free: 434.4 MiB)
25/11/30 04:41:21 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on 172.20.0.3:42151 (size: 35.1 KiB, free: 434.4 MiB)
25/11/30 04:41:21 INFO TaskSetManager: Finished task 0.0 in stage 2.0 (TID 2) in 740 ms on 172.20.0.3 (executor 0) (1/1)
25/11/30 04:41:21 INFO TaskSchedulerImpl: Removed TaskSet 2.0, whose tasks have all completed, from pool 
25/11/30 04:41:21 INFO DAGScheduler: ResultStage 2 (showString at NativeMethodAccessorImpl.java:0) finished in 0.764 s
25/11/30 04:41:21 INFO DAGScheduler: Job 2 is finished. Cancelling potential speculative or zombie tasks for this job
25/11/30 04:41:21 INFO TaskSchedulerImpl: Killing all running tasks in stage 2: Stage finished
25/11/30 04:41:21 INFO DAGScheduler: Job 2 finished: showString at NativeMethodAccessorImpl.java:0, took 0.766114 s
+--------------------+
|     riyadh_geometry|
+--------------------+
|POINT (45.1332784...|
|POINT (45.251864 ...|
|POINT (45.3831482...|
|POINT (46.010629 ...|
|POINT (45.199444 ...|
|POINT (45.41075 2...|
|POINT (45.4107609...|
|POINT (45.4169158...|
|POINT (45.5054344...|
|POINT (45.552073 ...|
+--------------------+

25/11/30 04:41:21 INFO SparkContext: SparkContext is stopping with exitCode 0.
25/11/30 04:41:21 INFO SparkUI: Stopped Spark web UI at http://9515d4ca2c5d:4040
25/11/30 04:41:21 INFO StandaloneSchedulerBackend: Shutting down all executors
25/11/30 04:41:21 INFO StandaloneSchedulerBackend$StandaloneDriverEndpoint: Asking each executor to shut down
25/11/30 04:41:21 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
25/11/30 04:41:21 INFO MemoryStore: MemoryStore cleared
25/11/30 04:41:21 INFO BlockManager: BlockManager stopped
25/11/30 04:41:21 INFO BlockManagerMaster: BlockManagerMaster stopped
25/11/30 04:41:21 INFO OutputCommitCoordinator$OutputCommitCoordinatorEndpoint: OutputCommitCoordinator stopped!
25/11/30 04:41:21 INFO SparkContext: Successfully stopped SparkContext
25/11/30 04:41:21 INFO ShutdownHookManager: Shutdown hook called
25/11/30 04:41:21 INFO ShutdownHookManager: Deleting directory /tmp/spark-bdc8d352-376d-48af-97d5-1e8acdf68155/pyspark-a2946f51-a6e0-4504-bea4-94f7e33925a0
25/11/30 04:41:21 INFO ShutdownHookManager: Deleting directory /tmp/spark-bdc8d352-376d-48af-97d5-1e8acdf68155
25/11/30 04:41:21 INFO ShutdownHookManager: Deleting directory /tmp/spark-97275899-cefb-4c9e-831f-65e7af755df1
```