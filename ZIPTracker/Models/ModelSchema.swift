import Foundation
import SwiftData

/// Versioned SwiftData schema for ZIP Tracker.
///
/// All persistence goes through a `VersionedSchema` + `SchemaMigrationPlan` so
/// that future model changes can ship a migration stage instead of silently
/// breaking existing on-device stores. v1 is the shipping baseline.
///
/// When you change a model:
/// 1. Add `ZIPTrackerSchemaV2` (copy the changed model types into it).
/// 2. Append it to `ZIPTrackerMigrationPlan.schemas`.
/// 3. Add a `MigrationStage` (`.lightweight` or `.custom`) describing V1 → V2.
enum ZIPTrackerSchemaV1: VersionedSchema {
    static var versionIdentifier = Schema.Version(1, 0, 0)

    static var models: [any PersistentModel.Type] {
        [TrackedZCTA.self, ZCTAVisit.self, TrackingEventLog.self, AppSettings.self]
    }
}

/// The ordered list of schema versions and the stages that connect them.
enum ZIPTrackerMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] {
        [ZIPTrackerSchemaV1.self]
    }

    static var stages: [MigrationStage] {
        // No migrations yet — v1 is the baseline. Add stages here for V1 → V2…
        []
    }
}

/// Convenience accessor for the current (latest) schema used to build the
/// `ModelContainer`.
enum ZIPTrackerSchema {
    static var current: Schema { Schema(versionedSchema: ZIPTrackerSchemaV1.self) }
    static var migrationPlan: SchemaMigrationPlan.Type { ZIPTrackerMigrationPlan.self }
}
