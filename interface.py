import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

class PymemdynReport:
    """
    Class to interact with report-data from PyMemDyn output.
    """
    def __init__(self, report_directory: str):
        """
        Initializes the ReportAnalyzer with the path to the report's directory.
        :param report_directory: Path to the report subdirectory (e.g., './reports/4EIY')
        """
        self.report_directory = report_directory
        self.pdbcode = self.report_directory[-4:]
        self.xvg_files = self._get_xvg_files()  # List of .xvg files in the directory

        # split .xvg files in rmsX (e.g. 'rmsd-backbone...') & 'system' files (e.g. 'pressure')
        self.rmsx_xvg_files = [x for x in self.xvg_files if x.startswith('rms')] 
        self.sys_xvg_files = set(self.xvg_files) - set(self.rmsx_xvg_files)

    def _get_xvg_files(self):
        """
        Returns a list of all .xvg files in the report directory.
        """
        xvgs = [f for f in os.listdir(self.report_directory) if f.endswith('.xvg')]
        rmsX_items = sorted([item for item in xvgs if item.startswith('rms')])
        non_rmsX_items = sorted([item for item in xvgs if not item.startswith('rms')])
        sorted_xvgs = rmsX_items + non_rmsX_items
        return sorted_xvgs

    def load_data(self, filename: str):
        """
        Loads the .xvg file into numpy arrays, skipping comment lines starting with '#' or '@'.
        :param filename: Name of the .xvg file to load
        :return: Two numpy arrays (x, y)
        """
        file_path = os.path.join(self.report_directory, filename)
        x, y = np.loadtxt(file_path, comments=["#", "@"], unpack=True)
        return x, y

    def plot(self, selection=None):
        """
        Creates a subplot for each .xvg data file and displays them in a single figure.
        :param selection: .xvg data to plot: 'system', 'residualmeans', or None to plot all .xvg's.
        """
        if selection == 'system':
            data_to_plot = self.sys_xvg_files
        elif selection == 'residualmeans':
            data_to_plot = self.rmsx_xvg_files
        elif selection is None:
            data_to_plot = self.xvg_files
        else:
            return ValueError(f'{selection} is not a valid data selection (\'system\', \'residualmeans\', or None to plot all)')

        self._xy_plotlabels = {
            'rmsd-all-atom-vs-start.xvg': ['Time (ps)', 'RMSD (nm)'],
            'rmsd-backbone-vs-start.xvg': ['Time (ps)', 'RMSD (nm)'],
            'rmsd-calpha-vs-start.xvg': ['Time (ps)', 'RMSD (nm)'],
            'rmsf-per-residue.xvg': ['Residue number', 'RMS fluctuation (nm)'],
            'pressure.xvg': ['Time (ps)', 'Pressure (bar)'],
            'volume.xvg': ['Time (ps)', 'Volume (nm^3)'],
            'temp.xvg': ['Time (ps)', 'Temperature (K)'],
            'tot_ener.xvg': ['Time (ps)', 'Total Energy (kJ/mol)']
        }

        # Determine the number of rows and columns for the subplots (e.g., 4x4 grid)
        nplots = len(data_to_plot)
        ncols = 4  # Fixed number of columns (4 for 4x4 grid)
        nrows = (nplots + ncols - 1) // ncols  # Calculate the number of rows needed

        # set figure size based on data selection (double / single row)
        if data_to_plot == self.xvg_files:
            fs = (15, 10)
        else:
            fs = (15, 5)

        # Create a figure with subplots
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=fs)
        axes = axes.flatten()  # Flatten axes array to easily iterate over subplots
        fig.suptitle(f"{self.report_directory[-4:]}", x=0.5, fontsize=16, fontweight='bold')

        # Loop through each .xvg file and plot on its own subplot
        for i, xvg_file in enumerate(data_to_plot):
            x, y = self.load_data(xvg_file)
            ax = axes[i]  # Select the subplot
            ax.plot(x, y)
            if selection == 'residualmeans':
                if xvg_file != 'rmsf-per-residue.xvg':
                    ax.axvline(x=0, color='r', linestyle='--', alpha=0.3, label='Heavy atoms relax. 1000 kJ/mol/nm^2')
                    ax.axvline(x=500, color='r', linestyle='--', alpha=0.3, label='Heavy atoms relax. 800 kJ/mol/nm^2')
                    ax.axvline(x=1000, color='r', linestyle='--', alpha=0.3, label='Heavy atoms relax. 600 kJ/mol/nm^2')
                    ax.axvline(x=1500, color='r', linestyle='--', alpha=0.3, label='Heavy atoms relax. 400 kJ/mol/nm^2')
                    ax.axvline(x=2000, color='r', linestyle='--', alpha=0.3, label='Heavy atoms relax. 200 kJ/mol/nm^2')
                    ax.axvline(x=2500, color='g', linestyle='--', alpha=0.3, label='BW relaxation')

                # if xvg_file == 'rmsd-all-atom-vs-start':
                #     lines_labels = ax.get_legend_handles_labels()
                #     lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
                #     fig.legend(lines, labels)

            ax.set_title(xvg_file.replace('.xvg', ''))
            
            # set labels based on dict
            ax.set_xlabel(f'{self._xy_plotlabels.get(xvg_file)[0]}')
            ax.set_ylabel(f'{self._xy_plotlabels.get(xvg_file)[1]}')


        # Remove any empty subplots (if the number of files doesn't fill the grid)
        for i in range(nplots, len(axes)):
            fig.delaxes(axes[i])


        plt.tight_layout()
            
        plt.show()
