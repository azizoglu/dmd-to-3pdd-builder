# 3PDD Dataset Builder

A tool for building the **3 Perspective Driver Dataset (3PDD)** from the Driver Monitoring Dataset (DMD).

## About

The **3 Perspective Driver Dataset (3PDD)** is built using one of the most comprehensive datasets in the literature: the **Driver Monitoring Dataset (DMD)**. We extend our sincere gratitude to [Vicomtech](https://www.vicomtech.org/) for their invaluable contribution to the driver monitoring research community.

The DMD is a multi-modal dataset specifically designed for Driver Monitoring Systems (DMS), featuring synchronized recordings from multiple cameras (body, face, hands) and multiple streams (RGB, Depth, IR) in real car and driving simulator scenarios.

### The 3PDD Dataset: A Balanced Multi-Modal Dataset for Driver Distraction Detection

The 3PDD dataset represents a carefully curated and balanced multi-perspective dataset designed for real-world driver distraction detection scenarios. Unlike other datasets in the literature, 3PDD offers a unique combination of features that make it particularly suitable for comprehensive driver monitoring research.

#### Multi-Perspective Architecture

3PDD captures driver behavior from three distinct camera perspectives:
- **Body Camera**: Full upper body view of the driver
- **Face Camera**: Face-focused view for detailed facial expression analysis
- **Hands Camera**: Hands and steering wheel view for gesture recognition

This multi-perspective approach enables comprehensive analysis of driver behavior from different angles, providing complementary information that significantly improves distraction detection accuracy.

#### Balanced Distribution of Distraction Behaviors

The dataset includes 10 different driver distraction behaviors, carefully balanced to ensure equal representation. Each behavior category contains exactly the same number of images across all three perspectives:

| Driver Distraction Behaviors | Body | Face | Hands | Total Images |
|------------------------------|------|------|-------|--------------|
| Drinking | 3825 | 3825 | 3825 | 11475 |
| Hair and makeup | 3825 | 3825 | 3825 | 11475 |
| Talking on the phone left | 3825 | 3825 | 3825 | 11475 |
| Talking on the phone right | 3825 | 3825 | 3825 | 11475 |
| Operating the radio | 3825 | 3825 | 3825 | 11475 |
| Reaching behind/side | 3825 | 3825 | 3825 | 11475 |
| Safe drive | 3825 | 3825 | 3825 | 11475 |
| Talking to passenger | 3825 | 3825 | 3825 | 11475 |
| Texting left | 3825 | 3825 | 3825 | 11475 |
| Texting right | 3825 | 3825 | 3825 | 11475 |
| **Total** | **38250** | **38250** | **38250** | **114750** |

This balanced distribution ensures that models trained on 3PDD do not suffer from class imbalance issues, leading to more robust and fair performance across all distraction categories.

#### Data Leakage Prevention Through Driver-Based Split

A critical feature of 3PDD is its rigorous approach to preventing data leakage. Each driver appears only in one of the three sets (training, validation, or testing), ensuring that the model never sees the same person during different phases:

- **Training Set**: 17 drivers × 135 images per driver = 2,295 images per class
- **Validation Set**: 5 drivers × 153 images per driver = 765 images per class  
- **Testing Set**: 5 drivers × 153 images per driver = 765 images per class

This driver-based split strategy ensures that the model generalizes to unseen individuals rather than simply memorizing specific drivers' characteristics, which is crucial for real-world deployment.

#### Real-World Applicability

3PDD is designed with real-world scenarios in mind, featuring several characteristics that distinguish it from other datasets:

1. **High-Quality Resolution**: Consistent image quality across all perspectives ensures reliable feature extraction
2. **Balanced Class Distribution**: Equal representation of all 10 distraction behaviors prevents model bias
3. **Driver-Based Split**: Eliminates data leakage and ensures true generalization capability
4. **Multi-Modal Organization**: Three synchronized perspectives for each scenario enable multi-view learning approaches
5. **Comprehensive Coverage**: 114,750 total images provide sufficient data for deep learning models

This unique combination makes 3PDD an invaluable resource for researchers developing robust, real-world driver monitoring systems.

### Learn More About DMD

- **GitHub Repository**: [Vicomtech/DMD-Driver-Monitoring-Dataset](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset)
- **Official Website**: [dmd.vicomtech.org](https://dmd.vicomtech.org/)

---

## Prerequisites

Before using this tool, you need to extract frames from DMD videos.

### Step 1: Extract Frames from DMD Videos

Use the official DMD **Dataset Explorer Tool (DEx)** to extract frames:

1. Visit: [exploreMaterial-tool](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset/tree/master/exploreMaterial-tool)
2. Follow the instructions to export frames from the video sequences
3. Organize the extracted frames in a source directory

### Step 2: Build 3PDD Dataset

Once you have extracted the frames, use this tool to organize them into the 3PDD structure.

---

## Installation

### Requirements

- Python 3.7+
- Required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

### Quick Start

Run the main script:

```bash
python build_3pdd_dataset.py
```

The tool will guide you through an interactive process:

1. **Source Directory**: Path to your extracted DMD frames
2. **Perspective Selection**: Choose which camera perspectives to include
3. **Structure Type**: Select the output directory structure

### Interactive Options

#### 1. Perspective Selection

Choose one or more camera perspectives:

- `body` - Full body camera view
- `face` - Face-focused camera view  
- `hands` - Hands and steering wheel view
- `All` - Include all three perspectives

**Example:**
```
Select perspectives:
  1. body
  2. face
  3. hands
  0. All
Choices (comma-separated): 1,2
```

#### 2. Structure Type

Choose how to organize the output dataset:

- **`split`** - Organized by perspective/split/class structure
  ```
  3pdd/
  ├── body/
  │   ├── train/
  │   │   ├── class_0/
  │   │   └── class_1/
  │   ├── val/
  │   └── test/
  ├── face/
  └── hands/
  ```

- **`flat`** - Organized by perspective/class structure (all splits merged)
  ```
  3pdd/
  ├── body/
  │   ├── class_0/
  │   └── class_1/
  ├── face/
  └── hands/
  ```

**Example:**
```
Structure type:
  1. split
  2. flat
Choice: 1
```

---

## Features

### High Performance

- **Parallel Processing**: Utilizes multi-core CPUs for fast indexing
- **Smart Indexing**: Handles millions of files efficiently
- **Real-time Progress**: Live updates during processing
- **Optimized for Large Datasets**: Designed to handle 50M+ files

### Flexible Matching

- **Exact filename matching**: Fast lookup for identical filenames
- **Normalized matching**: Handles variations in filenames (special characters, separators)

### Progress Tracking

```
Indexing: E:\DMD\DMD_Main_Dataset
Scanning directories for images...
Using 7 parallel workers

  Discovering: 1,234 dirs found (156 dirs/s) - 2,345,678 images indexed
  Finalizing: 1,234/1,234 (0 remaining) - 52,456,789 images

✓ Indexed: 52,456,789 images from 1,234 directories in 342.5s

Building split structure...

BODY:
  train: copied=15234, not_found=12
  val: copied=3456, not_found=2
  test: copied=3789, not_found=1

Complete! Output: C:\Users\...\3pdd
```

---

## Directory Structure

### Input Requirements

Your source directory should contain the extracted frames from DMD:

```
source_directory/
├── frame_0001.jpg
├── frame_0002.jpg
├── ...
└── frame_NNNN.jpg
```

### Output Structure

The tool reads perspective-specific image lists from the `image_lists/` directory:

```
image_lists/
├── body_train_images.txt
├── body_val_images.txt
├── body_test_images.txt
├── face_train_images.txt
├── face_val_images.txt
├── face_test_images.txt
├── hands_train_images.txt
├── hands_val_images.txt
└── hands_test_images.txt
```

---

## Class Mapping

The tool uses `class_to_idx.json` to map class indices to human-readable names. This ensures consistent class organization across all perspectives and splits.

---

## Performance Tips

### For Large Datasets (50M+ files)

1. **Use SSD Storage**: Significantly faster than HDD
2. **Adjust Workers**: Modify worker count if needed
   ```python
   indexer.index_directory(source_dir, max_workers=8)
   ```
3. **Monitor Progress**: The tool provides real-time updates every 1-2 seconds
4. **Check Disk Space**: Ensure sufficient space for the output dataset

### Expected Processing Times

| Files | Workers | Estimated Time |
|-------|---------|----------------|
| 1M    | 4       | ~2-3 minutes   |
| 10M   | 8       | ~15-20 minutes |
| 50M   | 8       | ~60-90 minutes |

*Times vary based on CPU, disk speed, and directory structure*

---

## Project Structure

```
dmd-to-3pdd-builder/
├── build_3pdd_dataset.py    # Main entry point
├── builders.py               # Dataset structure builders
├── copier.py                 # Image copying operations
├── file_utils.py             # File handling utilities
├── indexer.py                # Fast image indexing with parallel processing
├── models.py                 # Data models
├── parser.py                 # Text file parser
├── ui.py                     # User interface
├── class_to_idx.json         # Class mapping configuration
├── image_lists/              # Perspective-specific image lists
│   ├── body_train_images.txt
│   ├── body_val_images.txt
│   └── ...
└── README.md                 # This file
```

---

## Troubleshooting

### Issue: "Directory not found"
- Ensure the source directory path is correct
- Use absolute paths if relative paths don't work

### Issue: "Many images not found"
- Verify frames were extracted correctly using DEx tool
- Check that filenames in `.txt` files match extracted frames
- The tool will report how many images were not found

### Issue: "Process is slow"
- Check if you're using HDD instead of SSD
- Reduce `max_workers` if system is overloaded
- Close other resource-intensive applications

---

### Related Works

If using 3PDD for driver distraction detection, consider citing:

```bibtex
@article{meld3_2024,
  title={MELD3: Integrating Multi-Task Ensemble Learning for Driver Distraction Detection},
  author={[Authors]},
  journal={IEEE Access},
  year={2024},
  doi={10.1109/ACCESS.2024.3509033}
}
```

```bibtex
@inproceedings{ortega2020dmd,
  title={DMD: A Large-Scale Multi-modal Driver Monitoring Dataset for Attention and Alertness Analysis},
  author={Ortega, Juan Diego and Kose, Neslihan and Ca{\~n}as, Paola and Chao, Min-An and Unnervik, Alexander and Nieto, Marcos and Otaegui, Oihana and Salgado, Luis},
  booktitle={Computer Vision--ECCV 2020 Workshops},
  pages={387--405},
  year={2020},
  publisher={Springer},
  doi={10.1007/978-3-030-66823-5_23}
}
```

---

## Related Publications

1. **MELD3: Integrating Multi-Task Ensemble Learning for Driver Distraction Detection**  
   IEEE Access, 2024  
   DOI: [10.1109/ACCESS.2024.3509033](https://doi.org/10.1109/ACCESS.2024.3509033)

2. **DMD: A Large-Scale Multi-modal Driver Monitoring Dataset for Attention and Alertness Analysis**  
   ECCV 2020 Workshops  
   DOI: [10.1007/978-3-030-66823-5_23](https://doi.org/10.1007/978-3-030-66823-5_23)

---

## License

This tool is provided for research purposes. Please refer to the [DMD License](https://dmd.vicomtech.org/) for dataset usage terms.

---

## Acknowledgments

Special thanks to:

- **Vicomtech** for creating and maintaining the DMD dataset
- All contributors to the DMD project

---

## Support

For issues related to:
- **This tool**: Open an issue in this repository
- **DMD dataset**: Visit [DMD GitHub](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset)
- **Frame extraction**: Check [exploreMaterial-tool documentation](https://github.com/Vicomtech/DMD-Driver-Monitoring-Dataset/tree/master/exploreMaterial-tool)

---

**Developed with ❤️ by [ERUVision](https://vision.erciyes.edu.tr/) for the driver monitoring research community**