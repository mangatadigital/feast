package printer

import (
	"fmt"
	"strings"

	"github.com/gojek/feast/cli/feast/pkg/timeutil"
	"github.com/gojek/feast/protos/generated/go/feast/core"
)

// PrintFeatureDetail prints the details about the feature.
// Prints and returns the resultant formatted string.
func PrintFeatureDetail(featureDetail *core.UIServiceTypes_FeatureDetail) string {
	spec := featureDetail.GetSpec()
	lines := []string{
		fmt.Sprintf("%s:\t%s", "Id", spec.GetId()),
		fmt.Sprintf("%s:\t%s", "Entity", spec.GetEntity()),
		fmt.Sprintf("%s:\t%s", "Owner", spec.GetOwner()),
		fmt.Sprintf("%s:\t%s", "Description", spec.GetDescription()),
		fmt.Sprintf("%s:\t%s", "ValueType", spec.GetValueType()),
		fmt.Sprintf("%s:\t%s", "Uri", spec.GetUri()),
	}
	lines = append(lines, fmt.Sprintf("%s:\t%s", "Created", timeutil.FormatToRFC3339(*featureDetail.GetCreated())))
	lines = append(lines, fmt.Sprintf("%s:\t%s", "LastUpdated", timeutil.FormatToRFC3339(*featureDetail.GetLastUpdated())))
	if jobs := featureDetail.GetJobs(); len(jobs) > 0 {
		lines = append(lines, "Related Jobs:")
		for _, job := range jobs {
			lines = append(lines, fmt.Sprintf("- %s", job))
		}
	}
	if tags := spec.GetTags(); len(tags) > 0 {
		lines = append(lines, fmt.Sprintf("Tags: %s", strings.Join(tags, ",")))
	}
	out := strings.Join(lines, "\n")
	fmt.Println(out)
	return out
}

// PrintEntityDetail prints the details about the feature.
// Prints and returns the resultant formatted string.
func PrintEntityDetail(entityDetail *core.UIServiceTypes_EntityDetail) string {
	spec := entityDetail.GetSpec()
	lines := []string{
		fmt.Sprintf("%s:\t%s", "Name", spec.GetName()),
		fmt.Sprintf("%s:\t%s", "Description", spec.GetDescription()),
	}
	if tags := spec.GetTags(); len(tags) > 0 {
		lines = append(lines, fmt.Sprintf("Tags: %s", strings.Join(tags, ",")))
	}
	lines = append(lines, fmt.Sprintf("%s:\t%s", "LastUpdated", timeutil.FormatToRFC3339(*entityDetail.GetLastUpdated())))
	lines = append(lines, "Related Jobs:")
	for _, job := range entityDetail.GetJobs() {
		lines = append(lines, fmt.Sprintf("- %s", job))
	}
	out := strings.Join(lines, "\n")
	fmt.Println(out)
	return out
}

// PrintStorageDetail prints the details about the feature.
// Prints and returns the resultant formatted string.
// This function is deprecated, and may be removed in subsequent versions.
func PrintStorageDetail(storageDetail *core.UIServiceTypes_StorageDetail) string {
	spec := storageDetail.GetSpec()
	lines := []string{
		fmt.Sprintf("%s:\t%s", "Id", spec.GetId()),
		fmt.Sprintf("%s:\t%s", "Type", spec.GetType()),
		fmt.Sprintf("Options:"),
	}
	for k, v := range spec.GetOptions() {
		lines = append(lines, fmt.Sprintf("  %s: %s", k, v))
	}
	lines = append(lines, fmt.Sprintf("%s:\t%s", "LastUpdated", timeutil.FormatToRFC3339(*storageDetail.GetLastUpdated())))
	out := strings.Join(lines, "\n")
	fmt.Println(out)
	return out
}
