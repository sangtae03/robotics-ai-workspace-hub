# Robotics AI Workspace Hub

**로봇·Physical AI 관련 GitHub 저장소 222개 / 21개 분야**를 모았습니다. 개인화 추천이나 순위로 줄이지 않고, 개발 환경·스튜디오·ROS·AI 에이전트·시뮬레이터·정책·데이터·비전·계획·휴머노이드·드론·촉각 도구를 함께 공개합니다.

[검색 페이지 파일](index.html) · [전체 JSON](catalog.json) · [선택 다운로드](hub.py)

관련 모음: [웹 디자인·앱 개발 도구](https://github.com/sangtae03/design-app-dev-hub) · [PPT 제작 도구](https://github.com/sangtae03/ppt-tools-hub)

## 목록의 범위

- 확인일: **2026-11-26**. 저장소 **222개**, 분야 **21개**. 보관된 프로젝트도 삭제하지 않고 표시했습니다.
- 221개는 GitHub API 메타데이터로 원본 주소·설명·상태 등을 확인했습니다. ONNX Runtime은 원본 GitHub 웹 검색으로 확인했으며 API 조회 실패로 상태·시각·라이선스 필드는 비워뒀습니다.
- GitHub 전체를 빠짐없이 수록한 완전 목록은 아닙니다. 이번 확장 조사에서 확인한 목록입니다.
- 설명은 기능·용도 안내이며 설치·빌드·성능·실물 로봇 성공·SO-101/Thor 호환성을 전부 검증한 결과가 아닙니다.
- 로봇 전용 프로젝트와 일반 AI/최적화/환경 관리 기반 도구를 분야별로 구분했습니다. 확장 포크는 기능이 다른 구현이면 남겼습니다.
- 최근 push는 GitHub API의 UTC 시각으로 릴리스일이나 유지보수 품질 점수가 아닙니다.
- 원본 소스·모델·SDK·데이터·에셋은 각자의 라이선스와 접근 조건을 따릅니다. 미표시·NOASSERTION은 자유 사용 허가가 아닙니다.

## 분야별 바로가기

| 분야 | 키 | 개수 |
|---|---|---:|
| [개발 워크스페이스 · 컨테이너 · 클라우드](#sector-workspace) | `workspace` | 10 |
| [통합 스튜디오 · 웹 GUI · 운영 화면](#sector-studio) | `studio` | 10 |
| [ROS · 통신 · 하드웨어 연결](#sector-ros) | `ros` | 10 |
| [로봇 AI 에이전트 · 작업 실행](#sector-agents) | `agents` | 10 |
| [MCP · AI 도구 연결](#sector-mcp) | `mcp` | 10 |
| [물리 엔진 · 범용 시뮬레이터](#sector-physics) | `physics` | 10 |
| [조작 시뮬레이션 · 벤치마크](#sector-sim) | `sim` | 16 |
| [VLA · 범용 로봇 모델](#sector-vla) | `vla` | 12 |
| [모방학습 · 정책 · 실물 강화학습](#sector-learning) | `learning` | 12 |
| [강화학습 알고리즘 · 학습 인프라](#sector-rl) | `rl` | 10 |
| [데이터 · 로깅 · 검수](#sector-data) | `data` | 10 |
| [텔레옵 · 시연 수집 · 저가 로봇](#sector-teleop) | `teleop` | 10 |
| [경로 계획 · 최적 제어](#sector-planning) | `planning` | 10 |
| [기구학 · 도달 영역 · 로봇 모델](#sector-kinematics) | `kinematics` | 12 |
| [물체 인식 · 분할 · 시각 추론](#sector-vision) | `vision` | 10 |
| [깊이 · 3D · 파지 추정](#sector-depth) | `depth` | 10 |
| [SLAM · 이동로봇 · 지도](#sector-slam) | `slam` | 10 |
| [휴머노이드 · 사족보행 · 손](#sector-humanoid) | `humanoid` | 10 |
| [드론 · 자율주행 · 다중 로봇](#sector-drone) | `drone` | 10 |
| [배포 · 월드 모델 · 추가 탐색](#sector-deploy) | `deploy` | 15 |
| [촉각 센서 · 접촉 조작](#sector-tactile) | `tactile` | 5 |

## 검색 페이지

`index.html`은 외부 서비스 없이 목록 데이터를 포함하는 정적 페이지입니다. 내려받아 브라우저에서 열 수 있습니다. 처음에는 보관 항목을 포함한 **222개 전체**를 표시합니다. 이름·설명 검색, 분야 선택, 이름·최근 push·별 수 정렬을 지원합니다. 별 수는 추천 순위가 아닙니다.

## 소스 선택 다운로드

Python 3.10 이상과 Git이 필요합니다. 이 도구는 원본 소스만 clone하며 외부 코드·설치 스크립트를 실행하지 않습니다.

```bash
git clone https://github.com/sangtae03/robotics-ai-workspace-hub.git
cd robotics-ai-workspace-hub
python hub.py sectors
python hub.py list --category workspace
python hub.py fetch --category studio --dry-run
python hub.py fetch --repo RobotecAI/rai --dry-run
python hub.py fetch --repo RobotecAI/rai
python hub.py fetch --all --include-archived --dry-run
```

기본 경로: `tools/<owner>--<repo>/`. 기존 폴더는 건너뛰며 사용자의 수정 내용을 덮어쓰지 않습니다. `--dest 경로`로 바꿀 수 있습니다. 기본 선택에서는 보관됨을 제외하고 `--include-archived`로 포함합니다. 모델·LFS·하위 모듈·의존성은 각 원본 절차를 따릅니다.

## 전체 목록

**보관됨**: archived · **확장 포크**: GitHub fork 표시 · 목록 순서는 추천 순위가 아닙니다.

<a id="sector-workspace"></a>

### 개발 워크스페이스 · 컨테이너 · 클라우드 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [isaac-sim/IsaacSim-ros_workspaces](https://github.com/isaac-sim/IsaacSim-ros_workspaces) | Isaac Sim 공식 ROS Humble/Jazzy 작업공간 | — |
| [RoboStack/robostack](https://github.com/RoboStack/robostack) | Conda/Pixi 계열 ROS 배포 환경 | — |
| [prefix-dev/pixi](https://github.com/prefix-dev/pixi) | 프로젝트 환경·의존성·실행 작업 관리 | — |
| [openrosde/openrosde](https://github.com/openrosde/openrosde) | 컨테이너 기반 로봇 개발 환경 | — |
| [isaac-sim/IsaacAutomator](https://github.com/isaac-sim/IsaacAutomator) | 클라우드 Isaac 워크스테이션 구성 | — |
| [isaac-sim/isaac-launchable](https://github.com/isaac-sim/isaac-launchable) | Isaac·VS Code 사전 구성 클라우드 환경 | — |
| [BerkeleyAutomation/FogROS2](https://github.com/BerkeleyAutomation/FogROS2) | ROS 2 클라우드·분산 실행 | — |
| [NVIDIA-ISAAC-ROS/isaac_ros_common](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_common) | Isaac ROS 공통 실행·개발 도구 | — |
| [NVIDIA/OSMO](https://github.com/NVIDIA/OSMO) | 학습·시뮬·실물 시험 워크플로 관리 | — |
| [osrf/rocker](https://github.com/osrf/rocker) | ROS·GUI·장치용 Docker 실행 보조 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-studio"></a>

### 통합 스튜디오 · 웹 GUI · 운영 화면 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [huggingface/leLab](https://github.com/huggingface/leLab) | LeRobot 설정·수집·학습 웹 GUI | — |
| [TheMomentLab/LeStudio](https://github.com/TheMomentLab/LeStudio) | 로봇팔 장치 설정·운영 웹 GUI | — |
| [phospho-app/phosphobot](https://github.com/phospho-app/phosphobot) | 로봇 제어·수집·학습 UI/API | — |
| [open-edge-platform/physical-ai-studio](https://github.com/open-edge-platform/physical-ai-studio) | 시연·학습·평가·추론 통합 화면 | — |
| [HorizonRobotics/RoboOrchard](https://github.com/HorizonRobotics/RoboOrchard) | 실물 조작·텔레옵·데이터 통합 | — |
| [foxglove/studio](https://github.com/foxglove/studio) | 로봇 데이터 시각화 Studio 원본 | **보관됨** |
| [lichtblick-suite/lichtblick](https://github.com/lichtblick-suite/lichtblick) | 로봇 로그·센서 시각화 GUI | — |
| [dora-rs/gsoc2026-dora-studio](https://github.com/dora-rs/gsoc2026-dora-studio) | Dora 파이프라인 실행·디버그 GUI | — |
| [matthewwoodc0/lerobot-gui-wrapper](https://github.com/matthewwoodc0/lerobot-gui-wrapper) | LeRobot 로컬 작업·실험 관리 화면 | — |
| [NeodyD/RoboCopilot-X](https://github.com/NeodyD/RoboCopilot-X) | ROS·MoveIt·URDF용 AI 개발 보조 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-ros"></a>

### ROS · 통신 · 하드웨어 연결 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [ros2/ros2](https://github.com/ros2/ros2) | ROS 2 전체 소스 작업공간 목록 | — |
| [ros2/rclpy](https://github.com/ros2/rclpy) | ROS 2 Python 클라이언트 | — |
| [ros2/rclcpp](https://github.com/ros2/rclcpp) | ROS 2 C++ 클라이언트 | — |
| [ros-controls/ros2_control](https://github.com/ros-controls/ros2_control) | 로봇 하드웨어·제어기 통합 | — |
| [ros-controls/ros2_controllers](https://github.com/ros-controls/ros2_controllers) | ROS 2 표준 제어기 | — |
| [RobotWebTools/rosbridge_suite](https://github.com/RobotWebTools/rosbridge_suite) | ROS WebSocket·JSON 브리지 | — |
| [micro-ROS/micro_ros_setup](https://github.com/micro-ROS/micro_ros_setup) | 마이크로컨트롤러 ROS 환경 구성 | — |
| [eclipse-zenoh/zenoh](https://github.com/eclipse-zenoh/zenoh) | 로봇·분산 데이터 통신 | — |
| [eclipse-cyclonedds/cyclonedds](https://github.com/eclipse-cyclonedds/cyclonedds) | DDS 통신 미들웨어 | — |
| [eProsima/Fast-DDS](https://github.com/eProsima/Fast-DDS) | DDS 통신 미들웨어 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-agents"></a>

### 로봇 AI 에이전트 · 작업 실행 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [RobotecAI/rai](https://github.com/RobotecAI/rai) | ROS 2 기반 Physical AI 에이전트 | — |
| [dimensionalOS/dimos](https://github.com/dimensionalOS/dimos) | 인지·행동·자연어 연결 런타임 | — |
| [dora-rs/dora](https://github.com/dora-rs/dora) | 로봇 AI 데이터 흐름 런타임 | — |
| [HorizonRobotics/HoloAgent](https://github.com/HorizonRobotics/HoloAgent) | 인지·이동·조작 통합 에이전트 | — |
| [terminalworld/OpenRUA](https://github.com/terminalworld/OpenRUA) | 코딩 에이전트의 로봇 도구 실행 | — |
| [fast-rua/ORA](https://github.com/fast-rua/ORA) | 카메라·도구 기반 로봇 사용 에이전트 | — |
| [OpenMOSS/OpenETA](https://github.com/OpenMOSS/OpenETA) | 인지·행동·검증·학습 루프 | — |
| [strands-labs/robots](https://github.com/strands-labs/robots) | 로봇용 에이전트·정책 통합 | — |
| [NVlabs/VoLoAgent](https://github.com/NVlabs/VoLoAgent) | 시각·언어 기반 조작 실행 | — |
| [NVlabs/ENPIRE](https://github.com/NVlabs/ENPIRE) | 인지·계획·로봇 조작 연구 환경 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-mcp"></a>

### MCP · AI 도구 연결 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [robotmcp/ros-mcp-server](https://github.com/robotmcp/ros-mcp-server) | rosbridge 기반 AI·ROS 연결 | — |
| [wise-vision/ros2_mcp](https://github.com/wise-vision/ros2_mcp) | rclpy 기반 ROS 2 MCP | — |
| [LCAS/ros2_mcp](https://github.com/LCAS/ros2_mcp) | ROS 2 그래프·센서 조회 도구 | — |
| [gtoff/moveit-mcp-server](https://github.com/gtoff/moveit-mcp-server) | MoveIt 계획·실행 MCP | — |
| [ajtudela/nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server) | Nav2 목적지·경로 관리 MCP | — |
| [whats2000/isaacsim-mcp-server](https://github.com/whats2000/isaacsim-mcp-server) | Isaac Sim 장면·센서·로봇 MCP | 확장 포크 |
| [GenRobo/isaac-sim-mcp](https://github.com/GenRobo/isaac-sim-mcp) | Isaac Sim 조작·실험 MCP | — |
| [Rongxuan-Zhou/mujoco-mcp-server](https://github.com/Rongxuan-Zhou/mujoco-mcp-server) | MuJoCo 물리·궤적 MCP | — |
| [Tibe31/so101-mcp](https://github.com/Tibe31/so101-mcp) | SO-101 관절·그리퍼 MCP | — |
| [IliaLarchenko/robot_MCP](https://github.com/IliaLarchenko/robot_MCP) | SO-100/101 로봇·카메라 MCP | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-physics"></a>

### 물리 엔진 · 범용 시뮬레이터 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [isaac-sim/IsaacSim](https://github.com/isaac-sim/IsaacSim) | Isaac Sim 소스·시뮬레이션 | — |
| [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco) | 접촉·관절 물리 엔진 | — |
| [newton-physics/newton](https://github.com/newton-physics/newton) | Warp 기반 GPU 물리 엔진 | — |
| [Genesis-Embodied-AI/genesis-world](https://github.com/Genesis-Embodied-AI/genesis-world) | 범용 Physical AI 시뮬레이션 | — |
| [bulletphysics/bullet3](https://github.com/bulletphysics/bullet3) | Bullet·PyBullet 물리 시뮬레이션 | — |
| [gazebosim/gz-sim](https://github.com/gazebosim/gz-sim) | Gazebo 로봇 시뮬레이터 | — |
| [cyberbotics/webots](https://github.com/cyberbotics/webots) | 범용 3D 로봇 시뮬레이터 | — |
| [RobotLocomotion/drake](https://github.com/RobotLocomotion/drake) | 동역학·제어·최적화 시뮬레이션 | — |
| [haosulab/SAPIEN](https://github.com/haosulab/SAPIEN) | 조작·관절 물체 시뮬레이션 | — |
| [google-deepmind/mujoco_warp](https://github.com/google-deepmind/mujoco_warp) | MuJoCo GPU 실행 기반 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-sim"></a>

### 조작 시뮬레이션 · 벤치마크 · 16개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) | 로봇 병렬 학습 환경 | — |
| [LightwheelAI/leisaac](https://github.com/LightwheelAI/leisaac) | SO-101 Isaac 텔레옵·학습 환경 | — |
| [mani-skill/ManiSkill](https://github.com/mani-skill/ManiSkill) | GPU 조작 학습·벤치마크 | — |
| [ARISE-Initiative/robosuite](https://github.com/ARISE-Initiative/robosuite) | MuJoCo 조작 환경 | — |
| [robocasa/robocasa](https://github.com/robocasa/robocasa) | 생활·주방 조작 환경 | — |
| [RoboTwin-Platform/RoboTwin](https://github.com/RoboTwin-Platform/RoboTwin) | 양팔 조작·데이터 생성 | — |
| [RoboVerseOrg/RoboVerse](https://github.com/RoboVerseOrg/RoboVerse) | 통합 로봇 시뮬·학습 플랫폼 | — |
| [HorizonRobotics/RoboOrchardSim](https://github.com/HorizonRobotics/RoboOrchardSim) | Isaac 기반 조작 시뮬레이션 | — |
| [isaac-sim/IsaacLab-Arena](https://github.com/isaac-sim/IsaacLab-Arena) | 작업 조합·정책 평가 | — |
| [google-deepmind/mujoco_playground](https://github.com/google-deepmind/mujoco_playground) | MuJoCo 로봇 학습·실물 예제 | — |
| [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) | 언어 조건 조작 벤치마크 | — |
| [mees/calvin](https://github.com/mees/calvin) | 장기 언어 조건 조작 벤치마크 | — |
| [stepjam/RLBench](https://github.com/stepjam/RLBench) | 시각 로봇 학습 작업 모음 | — |
| [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) | 로봇 정책 시뮬 평가 | — |
| [StanfordVL/BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K) | 생활 작업·환경 벤치마크 | — |
| [RoboDojo-Benchmark/RoboDojo](https://github.com/RoboDojo-Benchmark/RoboDojo) | 로봇 조작 정책 평가 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-vla"></a>

### VLA · 범용 로봇 모델 · 12개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | GR00T 범용 로봇 행동 모델 | — |
| [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | π 계열 정책·미세조정 | — |
| [openvla/openvla](https://github.com/openvla/openvla) | OpenVLA 학습·추론 | 확장 포크 |
| [moojink/openvla-oft](https://github.com/moojink/openvla-oft) | OpenVLA 최적화 미세조정 | 확장 포크 |
| [octo-models/octo](https://github.com/octo-models/octo) | 범용 로봇 정책 | — |
| [rail-berkeley/crossformer](https://github.com/rail-berkeley/crossformer) | 여러 기종을 위한 범용 정책 | — |
| [Robot-VLAs/RoboVLMs](https://github.com/Robot-VLAs/RoboVLMs) | VLM 기반 로봇 정책 프레임워크 | — |
| [OpenDriveLab/UniVLA](https://github.com/OpenDriveLab/UniVLA) | 잠재 행동 기반 VLA | — |
| [2toinf/X-VLA](https://github.com/2toinf/X-VLA) | 기종 간 VLA 정책 | — |
| [allenai/molmoact2](https://github.com/allenai/molmoact2) | MolmoAct2 로봇 행동 모델 | — |
| [allenai/molmoact](https://github.com/allenai/molmoact) | MolmoAct 원본 행동 모델 | — |
| [X-Square-Robot/wall-x](https://github.com/X-Square-Robot/wall-x) | Wall 계열 로봇 정책 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-learning"></a>

### 모방학습 · 정책 · 실물 강화학습 · 12개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [huggingface/lerobot](https://github.com/huggingface/lerobot) | 수집·데이터·학습·실물 배포 | — |
| [real-stanford/diffusion_policy](https://github.com/real-stanford/diffusion_policy) | Diffusion Policy 학습 | — |
| [tonyzhaozh/act](https://github.com/tonyzhaozh/act) | Action Chunking Transformer | — |
| [ARISE-Initiative/robomimic](https://github.com/ARISE-Initiative/robomimic) | 시연 기반 정책 학습 | — |
| [RLinf/RLinf](https://github.com/RLinf/RLinf) | 로봇 강화학습·후학습 인프라 | — |
| [rail-berkeley/hil-serl](https://github.com/rail-berkeley/hil-serl) | 사람 개입 실물 강화학습 | — |
| [rail-berkeley/serl](https://github.com/rail-berkeley/serl) | 실물 로봇 강화학습 기반 | — |
| [huggingface/gym-hil](https://github.com/huggingface/gym-hil) | 사람 개입 강화학습 환경 | — |
| [autoserl/AutoSERL](https://github.com/autoserl/AutoSERL) | 자동 개입 기반 실물 강화학습 연구 | — |
| [HorizonRobotics/RoboOrchardLab](https://github.com/HorizonRobotics/RoboOrchardLab) | 학습·평가 파이프라인 | — |
| [XPolicyLab/XPolicyLab](https://github.com/XPolicyLab/XPolicyLab) | 정책 서버·관측·행동·평가 연결 | — |
| [robometer/robometer](https://github.com/robometer/robometer) | 로봇 보상·진행도 모델 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-rl"></a>

### 강화학습 알고리즘 · 학습 인프라 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [DLR-RM/stable-baselines3](https://github.com/DLR-RM/stable-baselines3) | 범용 PyTorch 강화학습 | — |
| [vwxyzjn/cleanrl](https://github.com/vwxyzjn/cleanrl) | 간결한 강화학습 구현 | — |
| [leggedrobotics/rsl_rl](https://github.com/leggedrobotics/rsl_rl) | 로봇용 강화학습 라이브러리 | — |
| [Denys88/rl_games](https://github.com/Denys88/rl_games) | GPU 강화학습 라이브러리 | — |
| [Toni-SM/skrl](https://github.com/Toni-SM/skrl) | 모듈형 강화학습 라이브러리 | — |
| [ray-project/ray](https://github.com/ray-project/ray) | 분산 실행·학습·RLlib | — |
| [pytorch/rl](https://github.com/pytorch/rl) | TorchRL 강화학습 도구 | — |
| [google/brax](https://github.com/google/brax) | 가속 물리·강화학습 환경 | — |
| [thu-ml/tianshou](https://github.com/thu-ml/tianshou) | 범용 강화학습 프레임워크 | — |
| [Farama-Foundation/Gymnasium-Robotics](https://github.com/Farama-Foundation/Gymnasium-Robotics) | 로봇 강화학습 작업 환경 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-data"></a>

### 데이터 · 로깅 · 검수 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [rerun-io/rerun](https://github.com/rerun-io/rerun) | 영상·관절·좌표·점군 시각화 | — |
| [foxglove/mcap](https://github.com/foxglove/mcap) | 로봇 센서·메시지 기록 형식 | — |
| [foxglove/foxglove-sdk](https://github.com/foxglove/foxglove-sdk) | 로봇 데이터 시각화 SDK | — |
| [HorizonRobotics/RoboOrchardCore](https://github.com/HorizonRobotics/RoboOrchardCore) | 로봇 상태·변환·데이터 공통 구조 | — |
| [RoboticsData/score_lerobot_episodes](https://github.com/RoboticsData/score_lerobot_episodes) | LeRobot 에피소드 품질 점수화 | — |
| [Hebbian-Robotics/pareto](https://github.com/Hebbian-Robotics/pareto) | 로봇 시연 분석·검색·선별 | — |
| [google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment) | 기종 간 데이터셋·RT-X 자료 | — |
| [droid-dataset/droid](https://github.com/droid-dataset/droid) | 실물 조작 데이터 수집·활용 | — |
| [rail-berkeley/bridge_data_v2](https://github.com/rail-berkeley/bridge_data_v2) | BridgeData V2 데이터·학습 자료 | — |
| [NVlabs/mimicgen](https://github.com/NVlabs/mimicgen) | 시연 기반 데이터 증강·생성 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-teleop"></a>

### 텔레옵 · 시연 수집 · 저가 로봇 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [real-stanford/universal_manipulation_interface](https://github.com/real-stanford/universal_manipulation_interface) | 손에 든 그리퍼 기반 시연 수집 | — |
| [wuphilipp/gello_software](https://github.com/wuphilipp/gello_software) | GELLO 리더팔 텔레옵 | — |
| [tonyzhaozh/aloha](https://github.com/tonyzhaozh/aloha) | 저가 양팔 텔레옵 플랫폼 | — |
| [MarkFzp/mobile-aloha](https://github.com/MarkFzp/mobile-aloha) | 이동형 양팔 시연 플랫폼 | — |
| [aadhithya14/Open-Teach](https://github.com/aadhithya14/Open-Teach) | VR 기반 다기종 텔레옵 | — |
| [TheRobotStudio/SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) | SO-100/101 하드웨어·조립 | — |
| [adoodevv/so101_ros2](https://github.com/adoodevv/so101_ros2) | SO-101 ROS 2·MoveIt·실물 연결 | — |
| [sacovo/lerobot_ros](https://github.com/sacovo/lerobot_ros) | LeRobot·ROS 연결 후보 | — |
| [enactic/openarm](https://github.com/enactic/openarm) | 오픈 로봇팔 하드웨어·소프트웨어 | — |
| [unitreerobotics/xr_teleoperate](https://github.com/unitreerobotics/xr_teleoperate) | XR 장치 기반 Unitree 텔레옵 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-planning"></a>

### 경로 계획 · 최적 제어 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [moveit/moveit2](https://github.com/moveit/moveit2) | ROS 2 로봇팔 계획 프레임워크 | — |
| [NVlabs/curobo](https://github.com/NVlabs/curobo) | GPU IK·충돌·궤적 최적화 | — |
| [ompl/ompl](https://github.com/ompl/ompl) | 샘플링 기반 경로 계획 | — |
| [tesseract-robotics/tesseract](https://github.com/tesseract-robotics/tesseract) | 산업 로봇 계획·환경 모델 | — |
| [tesseract-robotics/trajopt](https://github.com/tesseract-robotics/trajopt) | 궤적 최적화 | — |
| [loco-3d/crocoddyl](https://github.com/loco-3d/crocoddyl) | 최적 제어·운동 계획 | — |
| [casadi/casadi](https://github.com/casadi/casadi) | 비선형 최적화·최적 제어 | — |
| [acados/acados](https://github.com/acados/acados) | 실시간 MPC 최적 제어 | — |
| [BehaviorTree/BehaviorTree.CPP](https://github.com/BehaviorTree/BehaviorTree.CPP) | 로봇 작업 행동 트리 | — |
| [splintered-reality/py_trees](https://github.com/splintered-reality/py_trees) | Python 행동 트리 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-kinematics"></a>

### 기구학 · 도달 영역 · 로봇 모델 · 12개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [stack-of-tasks/pinocchio](https://github.com/stack-of-tasks/pinocchio) | 기구학·동역학·미분 계산 | — |
| [Rhoban/placo](https://github.com/Rhoban/placo) | 작업·제약 기반 IK·동역학 | — |
| [kevinzakka/mink](https://github.com/kevinzakka/mink) | MuJoCo 미분 IK | — |
| [pink-kinematics/pink](https://github.com/pink-kinematics/pink) | Pinocchio 미분 IK | — |
| [petercorke/robotics-toolbox-python](https://github.com/petercorke/robotics-toolbox-python) | 로봇 기구학·계획 교육·분석 | — |
| [DLR-MO/reachability_map](https://github.com/DLR-MO/reachability_map) | 3D 도달 영역 계산 | — |
| [mrudorfer/rm4d](https://github.com/mrudorfer/rm4d) | 도달성 맵 | — |
| [compas-dev/compas_fab](https://github.com/compas-dev/compas_fab) | 로봇 제작·계획·도달성 | — |
| [clemense/yourdfpy](https://github.com/clemense/yourdfpy) | URDF 읽기·편집·시각화 | — |
| [robot-descriptions/robot_descriptions.py](https://github.com/robot-descriptions/robot_descriptions.py) | URDF·MJCF 로봇 모델 로딩 | — |
| [Rhoban/onshape-to-robot](https://github.com/Rhoban/onshape-to-robot) | CAD 조립품을 로봇 모델로 변환 | — |
| [OpenLegged/URDF-Studio](https://github.com/OpenLegged/URDF-Studio) | 웹 로봇 모델 편집·변환 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-vision"></a>

### 물체 인식 · 분할 · 시각 추론 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | 물체 검출·분할·추적 | — |
| [IDEA-Research/GroundingDINO](https://github.com/IDEA-Research/GroundingDINO) | 텍스트 조건 물체 검출 | — |
| [IDEA-Research/Grounded-SAM-2](https://github.com/IDEA-Research/Grounded-SAM-2) | 텍스트 검출·분할 연결 | — |
| [facebookresearch/sam2](https://github.com/facebookresearch/sam2) | 이미지·영상 분할 | — |
| [facebookresearch/sam3](https://github.com/facebookresearch/sam3) | 개념 조건 분할·추적 | — |
| [facebookresearch/dinov2](https://github.com/facebookresearch/dinov2) | 시각 특징 표현 | — |
| [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) | 손·얼굴·자세 인식 | — |
| [huggingface/transformers](https://github.com/huggingface/transformers) | VLM 등 모델 로딩·추론 기반 | — |
| [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | 시각·언어 이해 모델 | — |
| [roboflow/supervision](https://github.com/roboflow/supervision) | 비전 추론·추적·시각화 보조 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-depth"></a>

### 깊이 · 3D · 파지 추정 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [NVlabs/FoundationPose](https://github.com/NVlabs/FoundationPose) | 물체 6D 자세 추정·추적 | — |
| [NVlabs/FoundationStereo](https://github.com/NVlabs/FoundationStereo) | 스테레오 깊이 추정 | — |
| [NVlabs/Fast-FoundationStereo](https://github.com/NVlabs/Fast-FoundationStereo) | 고속 스테레오 깊이 추정 | — |
| [DepthAnything/Depth-Anything-V2](https://github.com/DepthAnything/Depth-Anything-V2) | 단안 깊이 추정 | — |
| [isl-org/Open3D](https://github.com/isl-org/Open3D) | 점군·정합·재구성 | — |
| [graspnet/graspnet-baseline](https://github.com/graspnet/graspnet-baseline) | 물체 파지 추정 기준 모델 | — |
| [graspnet/anygrasp_sdk](https://github.com/graspnet/anygrasp_sdk) | 파지 추정 SDK | — |
| [NVlabs/contact_graspnet](https://github.com/NVlabs/contact_graspnet) | 접촉 기반 파지 자세 생성 | — |
| [NVlabs/GraspGen](https://github.com/NVlabs/GraspGen) | 로봇 파지 생성 모델 | — |
| [PKU-EPIC/DexGraspNet](https://github.com/PKU-EPIC/DexGraspNet) | 다지 손 파지 데이터·생성 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-slam"></a>

### SLAM · 이동로봇 · 지도 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [ros-navigation/navigation2](https://github.com/ros-navigation/navigation2) | ROS 2 자율주행·경로·행동 | — |
| [SteveMacenski/slam_toolbox](https://github.com/SteveMacenski/slam_toolbox) | 2D SLAM·위치 추정 | — |
| [introlab/rtabmap_ros](https://github.com/introlab/rtabmap_ros) | RGB-D·LiDAR SLAM ROS 연결 | — |
| [UZ-SLAMLab/ORB_SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) | 시각·관성 SLAM | — |
| [hku-mars/FAST_LIO](https://github.com/hku-mars/FAST_LIO) | LiDAR·IMU 위치 추정 | — |
| [TixiaoShan/LIO-SAM](https://github.com/TixiaoShan/LIO-SAM) | LiDAR·관성 SLAM | — |
| [HKUST-Aerial-Robotics/VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion) | 시각·관성 센서 융합 | — |
| [PRBonn/kiss-icp](https://github.com/PRBonn/kiss-icp) | LiDAR 점군 오도메트리 | — |
| [NVIDIA-ISAAC-ROS/isaac_ros_visual_slam](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_visual_slam) | NVIDIA 가속 시각 SLAM | — |
| [NVIDIA-ISAAC-ROS/isaac_ros_nvblox](https://github.com/NVIDIA-ISAAC-ROS/isaac_ros_nvblox) | GPU 3D 재구성·지도 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-humanoid"></a>

### 휴머노이드 · 사족보행 · 손 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [leggedrobotics/legged_gym](https://github.com/leggedrobotics/legged_gym) | 사족·다리 로봇 강화학습 환경 | — |
| [unitreerobotics/unitree_rl_gym](https://github.com/unitreerobotics/unitree_rl_gym) | Unitree 학습·시뮬·배포 예제 | — |
| [unitreerobotics/unitree_mujoco](https://github.com/unitreerobotics/unitree_mujoco) | Unitree MuJoCo 시뮬레이션 | — |
| [MarkFzp/humanplus](https://github.com/MarkFzp/humanplus) | 사람 동작 추종·휴머노이드 모방 | — |
| [roboterax/humanoid-gym](https://github.com/roboterax/humanoid-gym) | 휴머노이드 강화학습 환경 | — |
| [LeCAR-Lab/HumanoidVerse](https://github.com/LeCAR-Lab/HumanoidVerse) | 휴머노이드 학습·다중 시뮬레이터 | — |
| [HorizonRobotics/HoloMotion](https://github.com/HorizonRobotics/HoloMotion) | 휴머노이드 전신 동작 학습 | — |
| [YanjieZe/GMR](https://github.com/YanjieZe/GMR) | 사람·로봇 동작 리타게팅 | — |
| [dexsuite/dex-retargeting](https://github.com/dexsuite/dex-retargeting) | 사람 손·로봇 손 리타게팅 | — |
| [dexsuite/dex-urdf](https://github.com/dexsuite/dex-urdf) | 다양한 로봇 손 URDF 모델 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-drone"></a>

### 드론 · 자율주행 · 다중 로봇 · 10개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [PX4/PX4-Autopilot](https://github.com/PX4/PX4-Autopilot) | 자율 비행 제어 | — |
| [ArduPilot/ardupilot](https://github.com/ArduPilot/ardupilot) | 드론·차량·선박 자동조종 | — |
| [mavlink/MAVSDK](https://github.com/mavlink/MAVSDK) | MAVLink 기반 로봇 제어 SDK | — |
| [mavlink/mavros](https://github.com/mavlink/mavros) | MAVLink·ROS 연결 | — |
| [bitcraze/crazyflie-firmware](https://github.com/bitcraze/crazyflie-firmware) | Crazyflie 드론 펌웨어 | — |
| [microsoft/AirSim](https://github.com/microsoft/AirSim) | Unreal 기반 드론·차량 시뮬레이션 | — |
| [iamaisim/ProjectAirSim](https://github.com/iamaisim/ProjectAirSim) | 드론·차량 AI 시뮬레이션 | — |
| [autowarefoundation/autoware](https://github.com/autowarefoundation/autoware) | 자율주행 소프트웨어 통합 | — |
| [carla-simulator/carla](https://github.com/carla-simulator/carla) | 자율주행 시뮬레이션 | — |
| [open-rmf/rmf](https://github.com/open-rmf/rmf) | 다중 로봇·플릿 관리 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-deploy"></a>

### 배포 · 월드 모델 · 추가 탐색 · 15개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [NVIDIA/TensorRT](https://github.com/NVIDIA/TensorRT) | NVIDIA 추론 최적화 | — |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 대규모 모델 추론 최적화 | — |
| [triton-inference-server/server](https://github.com/triton-inference-server/server) | GPU 모델 추론 서버 | — |
| [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) | 다중 플랫폼 모델 실행 | 웹 확인·API 상태 미확인 |
| [dusty-nv/jetson-containers](https://github.com/dusty-nv/jetson-containers) | Jetson AI 컨테이너 빌드·실행 | — |
| [nvidia-cosmos/cosmos-predict2](https://github.com/nvidia-cosmos/cosmos-predict2) | Physical AI 영상 월드 모델 | **보관됨** |
| [nvidia-cosmos/cosmos-reason2](https://github.com/nvidia-cosmos/cosmos-reason2) | 물리·공간 영상 추론 모델 | — |
| [NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) | Cosmos 월드 모델 생태계 | — |
| [backblaze-labs/awesome-physical-ai](https://github.com/backblaze-labs/awesome-physical-ai) | Physical AI 탐색 목록 | — |
| [fendouai/awesome-embodied-ai](https://github.com/fendouai/awesome-embodied-ai) | 로봇·모델·도구·데이터 대규모 목록 | — |
| [benchflow-ai/awesome-embodied-agents](https://github.com/benchflow-ai/awesome-embodied-agents) | 물리 세계 에이전트 탐색 목록 | — |
| [PyTorchKR/Awesome-Physical-AI](https://github.com/PyTorchKR/Awesome-Physical-AI) | Physical AI 분야별 자료 모음 | — |
| [nvidia-cosmos/cosmos-predict2.5](https://github.com/nvidia-cosmos/cosmos-predict2.5) | Cosmos 2.5 월드 모델·이전 세대; 제한적 유지보수 | — |
| [nvidia-cosmos/cosmos-transfer2.5](https://github.com/nvidia-cosmos/cosmos-transfer2.5) | 조건 기반 영상·도메인 변환 | — |
| [nvidia-cosmos/cosmos-cookbook](https://github.com/nvidia-cosmos/cosmos-cookbook) | Cosmos 후학습·활용 예제 | — |

[분야 목록으로](#분야별-바로가기)

<a id="sector-tactile"></a>

### 촉각 센서 · 접촉 조작 · 5개

| 저장소 | 역할 | 상태 |
|---|---|---|
| [facebookresearch/tacto](https://github.com/facebookresearch/tacto) | 시각 기반 촉각 센서 시뮬레이터 | **보관됨** |
| [gelsightinc/gsrobotics](https://github.com/gelsightinc/gsrobotics) | GelSight 로봇 촉각 센서 SDK | — |
| [robot-dexterity/tactile-gym](https://github.com/robot-dexterity/tactile-gym) | 촉각 관측 기반 강화학습 환경 | 확장 포크 |
| [robot-dexterity/tactile-sim](https://github.com/robot-dexterity/tactile-sim) | 촉각 센서·조작 시뮬레이션 | — |
| [univtac/UniVTAC](https://github.com/univtac/UniVTAC) | 시각·촉각 조작 학습 벤치마크 | — |

[분야 목록으로](#분야별-바로가기)

## 출처·수정

각 저장소명은 원본 GitHub로 연결됩니다. [catalog.json](catalog.json)에 확인 근거·API 주소·날짜·라이선스·보관 상태·fork 여부·최근 push를 기록했습니다. 수정할 때는 원본 문서와 메타데이터를 다시 확인하고 확인일을 갱신합니다.

허브 문서·도구는 MIT입니다. 원본 프로젝트를 같은 라이선스로 재배포하는 것은 아닙니다.
